# update()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Updates the fetched results.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@MainActor
@preconcurrency func update()
```

Available when `SectionIdentifier` conforms to `Hashable` and `Result` conforms to `NSFetchRequestResult`.

## Discussion

SwiftUI calls this function before rendering a view’s [`body`](../view/body-8kl5o.md) to ensure the view has the most recent fetched results.

## See Also

### Getting the fetched results
- [var wrappedValue: SectionedFetchResults<SectionIdentifier, Result>](./wrappedvalue.md)
  The fetched results of the fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/update())*