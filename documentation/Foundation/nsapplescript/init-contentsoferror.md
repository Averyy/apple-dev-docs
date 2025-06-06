# init(contentsOf:error:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated script instance from the source identified by the passed URL.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init?(contentsOf url: URL, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

#### Return Value

The initialized script object, `nil` if an error occurs.

#### Discussion

This method is a designated initializer for `NSAppleScript`.

## Parameters

- `url`: A URL that locates a script, in either text or compiled form.
- `errorInfo`: On return, if an error occurs, a pointer to an error information dictionary.

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
- [init?(source: String)](nsapplescript/init(source:).md)
  Initializes a newly allocated script instance from the passed source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsapplescript/init(contentsof:error:))*