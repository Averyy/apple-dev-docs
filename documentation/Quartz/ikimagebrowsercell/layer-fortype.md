# layer(forType:)

**Framework**: Quartz  
**Kind**: method

Returns a layer for the specified position.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func layer(forType type: String!) -> CALayer!
```

#### Return Value

The `CALayer` to display in the specified position.

#### Discussion

Subclasses can override this method to add a Core Animation layer to the cell

## Parameters

- `type`: A string representing the layer location. See   for possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowsercell/layer(fortype:))*