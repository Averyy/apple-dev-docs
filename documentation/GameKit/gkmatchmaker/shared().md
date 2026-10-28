# shared()

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Returns the singleton matchmaker instance.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func shared() -> GKMatchmaker
```

```objc
+ (GKMatchmaker *) sharedMatchmaker;
```

## Return Value

The shared matchmaker instance.

## Discussion

Games don’t create a `GKMatchmaker` object. Use this method instead to get the shared singleton instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmaker/shared())*