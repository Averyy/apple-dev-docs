# init(configuration:)

**Framework**: ExtensionFoundation  
**Kind**: init

Asynchronously finds an existing extension process or launches a one.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init(configuration: AppExtensionProcess.Configuration) async throws
```

#### Discussion

This initializer finds an existing extension process that matches the provided configuration object. If it’s unable to find an existing process, it launches a new extension process.

## Parameters

- `configuration`: The configuration options for the process to find or launch.

## See Also

- [init(configuration: AppExtensionProcess.Configuration) throws](appextensionprocess/init(configuration:)-2g0cy.md)
  Synchronously finds an existing extension process or launches a new one.
- [AppExtensionProcess.Configuration](appextensionprocess/configuration.md)
  An object that holds configuration options for an app extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess/init(configuration:)-38zf)*