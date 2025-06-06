# shared

**Framework**: AppKit  
**Kind**: property

Returns the shared `NSDocumentController` instance.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var shared: NSDocumentController { get }
```

#### Return Value

The shared `NSDocumentController` instance.

#### Discussion

If an `NSDocumentController` instance doesn’t exist yet, it is created.

Initialization reads in the document types from the `CFBundleDocumentTypes` property list (in `Info.plist`), registers the instance for [`willPowerOffNotification`](nsworkspace/willpoweroffnotification.md)s, and turns on the flag indicating that document user interfaces should be visible. You should always obtain your application’s `NSDocumentController` using this method.

## See Also

- [Document-Based App Programming Guide for Mac](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/DocBasedAppProgrammingGuideForOSX/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011179)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/shared)*