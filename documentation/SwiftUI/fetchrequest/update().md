# update()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Updates the fetched results.

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
@MainActor
@preconcurrency mutating func update()
```

Available when `Result` conforms to `NSFetchRequestResult`.

#### Discussion

SwiftUI calls this function before rendering a view’s [`body`](../view/body-8kl5o.md) to ensure the view has the most recent fetched results.

## See Also

### Getting the fetched results
- [var wrappedValue: FetchedResults<Result>](./wrappedvalue.md)
  The fetched results of the fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fetchrequest/update())*