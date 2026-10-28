# currentItemIdentifier

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An identifier of the current item.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var currentItemIdentifier: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * currentItemIdentifier;
```

## Discussion

The coordinator sets this value in a previous call to [`transitionToItem(withIdentifier:proposingInitialTimingBasedOn:)`](./transitiontoitem%28withidentifier,proposinginitialtimingbasedon%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator/currentitemidentifier)*