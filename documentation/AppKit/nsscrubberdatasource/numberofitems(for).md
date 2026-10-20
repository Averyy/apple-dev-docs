# numberOfItems(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the data source for the number of items in the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func numberOfItems(for scrubber: NSScrubber) -> Int
```

```objc
- (NSInteger) numberOfItemsForScrubber:(NSScrubber *) scrubber;
```

#### Return Value

The number of items in the scrubber.

## Parameters

- `scrubber`: The scrubber whose item count is being requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberdatasource/numberofitems(for:))*