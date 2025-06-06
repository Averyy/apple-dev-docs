# CMClockInvalidate(_:)

**Framework**: Core Media  
**Kind**: func

Stops the clock.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMClockInvalidate(_ clock: CMClock)
```

#### Discussion

After invalidation, the clock returns errors from all APIs. Only the owner of the clock should call this function.

## Parameters

- `clock`: The clock to stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclockinvalidate(_:))*