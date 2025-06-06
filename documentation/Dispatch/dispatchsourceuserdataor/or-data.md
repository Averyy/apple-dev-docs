# or(data:)

**Framework**: Dispatch  
**Kind**: method

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
func or(data: UInt)
```

#### Discussion

After you call this method, the dispatch source submits its event handler to its target queue to process the data. If you specify `0` for the data parameter, the dispatch source does not submit its event hander for execution.

## Parameters

- `data`: The value you want to merge with the existing data in the dispatch source. The dispatch source ORs this value with the currently pending data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsourceuserdataor/or(data:))*