# activeFindSession

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The object that manages the state, presentation, and behavior of an active search.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var activeFindSession: UIFindSession? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIFindSession * activeFindSession;
```

#### Discussion

This property returns the session object managing the details of the search. When no seach is active, [`isFindNavigatorVisible`](./isfindnavigatorvisible.md) is `false`, this returns `nil`.

## See Also

### Managing the search
- [func updateResultCount()](./updateresultcount%28%29.md)
  Updates the results the interface displays for the active search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteraction/activefindsession)*