# imageRepresentationType()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns the representation type of the image to display.

**Availability**:
- macOS

## Declaration

```swift
func imageRepresentationType() -> String!
```

```objc
- (NSString *) imageRepresentationType;
```

#### Return Value

A string that specifies the image representation type. The string can be any of the constants defined in [Image Representation Types](../../Quartz/image-representation-types.md).

#### Discussion

Your data source must implement this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagerepresentationtype())*