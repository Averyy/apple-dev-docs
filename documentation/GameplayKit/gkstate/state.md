# state

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Type Method

Creates a state object with the specified list of valid next states.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) state;
```

#### Return Value

A state object.

#### Discussion

Call this method to conveniently create instances of your custom state classes. To perform custom initialization in those classes, override the [`init()`](./init%28%29.md) initializer.

## See Also

### Creating a State
- [init()](./init%28%29.md)
  Initializes a state object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkstate/state)*