# replace(data:)

**Framework**: Dispatch  
**Kind**: method

Replaces the current pending data with the new value you provide.

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
func replace(data: UInt)
```

#### Discussion

After you call this method, the dispatch source submits its event handler to its target queue to process the data. If you specify `0` for the data parameter, the dispatch source does not submit its event hander for execution.

## Parameters

- `data`: The data that replaces the current pending value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceuserdatareplace/replace(data:))*