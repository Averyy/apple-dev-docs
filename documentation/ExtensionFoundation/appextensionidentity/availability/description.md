# description

**Framework**: ExtensionFoundation  
**Kind**: property  
**Role**: Instance Property

A string describing the extensions availability.

**Availability**:
- macOS 13.0+ - Deprecated in 26.0

> **Deprecated**: Replaced with AppExtensionPoint.Monitor

## Declaration

```swift
var description: String { get }
```

## See Also

### Accessing Availability Information
- [var totalCount: Int](./totalcount.md)
  The number of extensions not yet approved for hosting by the current app.
- [let disabledCount: Int](./disabledcount.md)
  The number of extensions disabled for hosting in the current app.
- [let enabledCount: Int](./enabledcount.md)
  The number of extensions enabled for hostng in the current app.
- [let unapprovedCount: Int](./unapprovedcount.md)
  The number of extensions not yet approved for hosing by the current app


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/availability/description)*