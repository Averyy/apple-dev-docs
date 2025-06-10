# max()

**Framework**: ActivityKit  
**Kind**: method

Returns the maximum element in an asynchronous sequence of comparable elements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@warn_unqualified_access
func max() async rethrows -> Self.Element?
```

#### Return Value

The sequence’s maximum element. If the sequence has no elements, returns `nil`.

#### Discussion

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `max()` method returns the max value of the sequence.

```swift
let max = await Counter(howHigh: 10)
    .max()
print(max ?? "none")
// Prints "10"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/contentstateupdates-swift.struct/max())*