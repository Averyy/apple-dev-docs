---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/troubleshooting"
framework: "swift-configuration/Configuration"
---

# Troubleshooting and access reporting

**Framework**: swift-configuration/Configuration  
**Role**: Article

Check out some techniques to debug unexpected issues and to increase visibility into accessed config values.

## Overview

### Debugging configuration issues

If you can’t read your configuration values correctly, check:

1. **Environment variable naming**: When using [`EnvironmentVariablesProvider`](./environmentvariablesprovider.md), the provider automatically converts keys to uppercase and replaces dots with underscores. For example, `database.url` becomes `DATABASE_URL`.
2. **Provider ordering**: When using multiple providers, the library checks them in order and the first one that returns a value wins.
3. **Debug with an access reporter**: Use access reporting to see which keys are being queried and what values (if any) are being returned. See the next section for details.

For guidance on selecting the right configuration access patterns and reader methods, check out [Choosing the access pattern](./choosing-access-patterns.md) and [Choosing reader methods](./choosing-reader-methods.md).

### Access reporting

Configuration access reporting can help you debug issues and understand which configuration values your application is using. Swift Configuration provides two built-in ways to log access ([`AccessLogger`](./accesslogger.md) and [`FileAccessLogger`](./fileaccesslogger.md)), and you can also implement your own [`AccessReporter`](./accessreporter.md).

#### Using AccessLogger

[`AccessLogger`](./accesslogger.md) integrates with Swift Log and records all configuration accesses:

```swift
let logger = Logger(label: "...")
let accessLogger = AccessLogger(logger: logger)
let config = ConfigReader(provider: provider, accessReporter: accessLogger)

// Each access will now be logged.
let timeout = config.double(forKey: "http.timeout", default: 30.0)
```

This produces log entries showing:

- Which configuration keys the code accessed.
- What values the provider returned (with secret values redacted).
- Which provider supplied the value.
- Whether the reader used default values.
- The location of the code reading the config value.
- The timestamp of the access.

#### Using FileAccessLogger

For writing access events to a file, especially useful during ad-hoc debugging, use [`FileAccessLogger`](./fileaccesslogger.md):

```swift
let fileLogger = try FileAccessLogger(filePath: "/var/log/myapp/config-access.log")
let config = ConfigReader(provider: provider, accessReporter: fileLogger)

// Each access will now be logged.
let timeout = config.double(forKey: "http.timeout", default: 30.0)
```

You can also enable file access logging for the whole application, without recompiling your code, by setting an environment variable:

```bash
export CONFIG_ACCESS_LOG_FILE=/var/log/myapp/config-access.log
```

And then read from the file to see one line per config access:

```bash
tail -f /var/log/myapp/config-access.log
```

### Error handling

#### Provider errors

If any provider throws an error during lookup:

- **Required methods** (`requiredString`, etc.): The method immediately throws the error to the caller.
- **Optional methods** (with or without defaults): The library handles the error gracefully, returning `nil` or the default value.

> 💡 **Tip**: Even when an error gets handled gracefully, you can log it using an [`AccessReporter`](./accessreporter.md).

#### Missing values

When no provider has the requested value:

- **Methods with defaults**: Return the provided default value.
- **Methods without defaults**: Return `nil`.
- **Required methods**: Throw an error.

#### File not found errors

File-based providers ([`FileProvider`](./fileprovider.md), [`ReloadingFileProvider`](./reloadingfileprovider.md), [`DirectoryFilesProvider`](./directoryfilesprovider.md), [`EnvironmentVariablesProvider`](./environmentvariablesprovider.md) with file path) can throw “file not found” errors when expected configuration files don’t exist.

Common scenarios and solutions:

**Optional configuration files:**

```swift
// Problem: App crashes when optional config file is missing
let provider = try await FileProvider<JSONSnapshot>(filePath: "/etc/optional-config.json")

// Solution: Use allowMissing parameter
let provider = try await FileProvider<JSONSnapshot>(
    filePath: "/etc/optional-config.json",
    allowMissing: true
)
```

**Environment-specific files:**

```swift
// Different environments may have different config files
let configPath = "/etc/\(environment)/config.json"
let provider = try await FileProvider<JSONSnapshot>(
    filePath: configPath,
    allowMissing: true  // Gracefully handle missing env-specific configs
)
```

**Container startup issues:**

```swift
// Config files might not be ready when container starts
let provider = try await ReloadingFileProvider<JSONSnapshot>(
    filePath: "/mnt/config/app.json",
    allowMissing: true  // Allow startup with empty config, load when available
)
```

> ❗ **Important**: The `allowMissing` parameter only affects missing files or directories. Files with syntax errors (invalid JSON, YAML, and so on) will still throw parsing errors.

### Reloading provider troubleshooting

#### Configuration not updating

If your reloading provider isn’t detecting file changes:

1. **Check ServiceGroup**: Run the provider in a `ServiceGroup`.
2. **Enable verbose logging**: The built-in providers use Swift Log for detailed logging, which can help spot issues.
3. **Verify file path**: Confirm the file path is correct, the file exists, and file permissions are correct.
4. **Check poll interval**: Consider if your poll interval is appropriate for your use case.

#### ServiceGroup integration issues

Common ServiceGroup problems:

```swift
// Incorrect: Provider not included in ServiceGroup
let provider = try await ReloadingFileProvider<JSONSnapshot>(filePath: "/etc/config.json")
let config = ConfigReader(provider: provider)
// File monitoring won't work

// Correct: Provider runs in ServiceGroup
let provider = try await ReloadingFileProvider<JSONSnapshot>(filePath: "/etc/config.json")
let serviceGroup = ServiceGroup(services: [provider], logger: logger)
try await serviceGroup.run()
```

For more details about reloading providers and ServiceLifecycle integration, see [Using reloading providers](./using-reloading-providers.md). To learn about proper configuration practices that can prevent common issues, check out [Adopting best practices](./best-practices.md).

## See Also

### Troubleshooting and access reporting
- [protocol AccessReporter](./accessreporter.md)
  A type that receives and processes configuration access events.
- [class AccessLogger](./accesslogger.md)
  An access reporter that logs configuration access events using the Swift Log API.
- [class FileAccessLogger](./fileaccesslogger.md)
  An access reporter that writes configuration access events to a file.
- [struct AccessEvent](./accessevent.md)
  An event that captures information about accessing a configuration value.
- [struct BroadcastingAccessReporter](./broadcastingaccessreporter.md)
  An access reporter that forwards events to multiple other reporters.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/troubleshooting)*