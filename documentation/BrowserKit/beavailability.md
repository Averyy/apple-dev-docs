# BEAvailability

**Framework**: BrowserKit  
**Kind**: class  
**Role**: Class

A class that tests whether a device is eligible to run an alternative browser engine.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
class BEAvailability
```

```objc
@interface BEAvailability : NSObject
```

## Topics

### Testing eligibility
- [class func isEligible(for: BEAvailability.Context, completionHandler: (Bool, (any Error)?) -> Void)](./beavailability/iseligible%28for,completionhandler%29.md)
  Tests whether the device is eligible to use an app that contains an alternative browser engine.
### Identifying contexts
- [BEAvailability.Context](./beavailability/context.md)
  The category of app for which you determine eligibility.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Essentials
- [Transferring browsing data to another browser](./transferring-browsing-data-to-another-browser.md)
  Allow people to transfer browsing history, bookmarks, reading lists, and browser extensions to or from your app using a system-provided sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beavailability)*