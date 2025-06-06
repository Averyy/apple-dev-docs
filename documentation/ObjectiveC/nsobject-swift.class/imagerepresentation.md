# imageRepresentation()

**Framework**: Objective-C Runtime  
**Kind**: method

Returns the image to display.

**Availability**:
- macOS ?+

## Declaration

```swift
func imageRepresentation() -> Any!
```

#### Return Value

The image to display; can return `nil` if the item has no image to display.

#### Discussion

Your data source must implement this method. This method  is called frequently, so the receiver should cache the returned instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagerepresentation())*