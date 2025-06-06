# imageUID()

**Framework**: Objective-C Runtime  
**Kind**: method

Returns a unique string that identifies the data source item.

**Availability**:
- macOS ?+

## Declaration

```swift
func imageUID() -> String!
```

#### Return Value

The string that identifies the data source item

#### Discussion

Your data source must implement this method. The image browser view uses this identifier to associate the data source item and  its cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imageuid())*