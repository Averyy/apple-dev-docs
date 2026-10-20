# reset()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Resets the command to its default state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func reset()
```

```objc
- (void) reset;
```

#### Discussion

A command that has been reset loses any state that you previously set and does nothing when executed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/reset())*