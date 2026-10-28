# maxNumberOfRecipients()

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Returns the maximum number of recipients permitted in a single request.

**Availability**:
- iOS 4.2+ - Deprecated in 10.0
- iPadOS 4.2+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.12
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: No longer supported.

## Declaration

```swift
class func maxNumberOfRecipients() -> Int
```

```objc
+ (NSUInteger) maxNumberOfRecipients;
```

## Return Value

The maximum number of recipients.

## Discussion

If you add more recipients than the value returned from this method, GameKit throws an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/maxnumberofrecipients())*