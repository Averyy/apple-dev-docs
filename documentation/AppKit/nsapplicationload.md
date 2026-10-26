# NSApplicationLoad

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Startup function to call when running Cocoa code from a Carbon application.

**Availability**:
- macOS

## Declaration

```c
extern BOOL NSApplicationLoad();
```

#### Return Value

[`true`](../Swift/true.md) if the [`NSApplication`](./nsapplication.md) object was successfully initialized and can now be used from your Carbon application or [`false`](../Swift/false.md) if there was an error during initialization.

#### Discussion

You typically call this function before calling other Cocoa code in a plug-in loaded into a primarily Carbon application. If the shared [`NSApplication`](./nsapplication.md) object isn’t already initialized, this function initializes it and sets up the necessary event handlers for Cocoa.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationload)*