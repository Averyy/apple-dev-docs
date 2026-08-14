# BEAvailability

**Framework**: BrowserKit  
**Kind**: class

A class that tests whether a device is eligible to run an alternative browser engine.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
class BEAvailability
```

## Topics

### Testing eligibility
- [class func isEligible(for: BEAvailability.Context, completionHandler: (Bool, (any Error)?) -> Void)](beavailability/iseligible(for:completionhandler:).md)
  Tests whether the device is eligible to use an app that contains an alternative browser engine.
### Identifying contexts
- [BEAvailability.Context](beavailability/context.md)
  The category of app for which you determine eligibility.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Transferring browsing data to another browser](transferring-browsing-data-to-another-browser.md)
  Allow people to transfer browsing history, bookmarks, reading lists, and browser extensions to or from your app using a system-provided sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beavailability)*