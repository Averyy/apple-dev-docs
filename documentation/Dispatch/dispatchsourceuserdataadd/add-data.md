# add(data:)

**Framework**: Dispatch  
**Kind**: method

Adds the value to the current pending data.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func add(data: UInt)
```

#### Discussion

After you call this method, the dispatch source submits its event handler to its target queue to process the data. If you specify `0` for the data parameter, the dispatch source does not submit its event hander for execution.

## Parameters

- `data`: The value you want to add the dispatch source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceuserdataadd/add(data:))*