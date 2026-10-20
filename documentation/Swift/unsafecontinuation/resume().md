# resume()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Resume the task that’s awaiting the continuation by returning.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func resume() where T == ()
```

Available when `E` conforms to `Error`.

#### Discussion

A continuation must be resumed exactly once. If the continuation has already resumed, then calling this method results in undefined behavior.

After calling this method, control immediately returns to the caller. The task continues executing when its executor schedules it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafecontinuation/resume())*