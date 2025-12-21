# init(configuration:)

**Framework**: ExtensionFoundation  
**Kind**: init

Finds an existing process for the specified app extension or creates a new one synchronously.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+
- tvOS 26.0+
- visionOS 1.1+
- watchOS 26.0+

## Declaration

```swift
init(configuration: AppExtensionProcess.Configuration) throws
```

#### Discussion

Use this initializer to request a process for the specified app extension and wait for the results. If a process for the extension already exists, the returned type uses that process. If no process exists, the system creates one and runs the app extension’s startup code before returning.

After receiving an instance of this type, use its methods to configure an XPC connection to the app extension. The system gives the app extension’s process enough runtime for your app to establish a connection. If you don’t create a connection right away, the system eventually suspends the app extension’s process. The system resumes the process again if you later try to create an XPC connection to it.

## Parameters

- `configuration`: A type that contains the identity of the app extension and additional   configuration details. The initializer copies the information it needs from your configuration   structure and doesn’t maintain a reference to it.

## See Also

- [init(configuration: AppExtensionProcess.Configuration) async throws](appextensionprocess/init(configuration:)-38zf.md)
  Finds an existing process for the specified app extension or creates a new one asynchronously.
- [AppExtensionProcess.Configuration](appextensionprocess/configuration.md)
  A structure that holds the identity of an app extension and process-related details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess/init(configuration:)-2g0cy)*