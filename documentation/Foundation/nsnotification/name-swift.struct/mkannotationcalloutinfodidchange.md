# MKAnnotationCalloutInfoDidChange

**Framework**: Foundation  
**Kind**: property

A property to observe to determine when the title or subtitle information of an annotation object changes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let MKAnnotationCalloutInfoDidChange: NSNotification.Name
```

#### Discussion

This notification supports legacy applications and is no longer necessary. MapKit tracks changes to the title and subtitle of an annotation using KVO notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/mkannotationcalloutinfodidchange)*