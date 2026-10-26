---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileaccesslogger/init(filepath:timezone:)"
framework: "swift-configuration/Configuration"
---

# init(filePath:timeZone:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a new file access logger that writes to the specified file path.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
convenience init(filePath: FilePath, timeZone: TimeZone = .current) throws
```

#### Discussion

The file and any necessary parent directories will be created if they don’t exist. If the file already exists, new entries will be appended to it.

```swift
// Log to a specific file
let logger = try FileAccessLogger(filePath: "/var/log/config-access.log")

// Log with custom timezone
let logger = try FileAccessLogger(
    filePath: "/tmp/access.log",
    timeZone: TimeZone(identifier: "UTC")!
)
```

> **Throws**: An error if the file cannot be created or opened for writing.

## Parameters

- `filePath`: The file path where access events will be written.
- `timeZone`: The time zone for timestamp formatting. Defaults to the current system timezone.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileaccesslogger/init(filepath:timezone:))*