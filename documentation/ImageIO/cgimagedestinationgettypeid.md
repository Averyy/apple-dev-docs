# CGImageDestinationGetTypeID()

**Framework**: Image I/O  
**Kind**: func

Returns the unique type identifier of an image destination opaque type.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGImageDestinationGetTypeID() -> CFTypeID
```

#### Return Value

Returns the Core Foundation type ID for an image destination.

#### Discussion

A type identifier is an integer that identifies the opaque type to which a Core Foundation object belongs. You use type IDs in various contexts, such as when you are operating on heterogeneous collections.

## See Also

- [func CGImageDestinationCopyTypeIdentifiers() -> CFArray](cgimagedestinationcopytypeidentifiers().md)
  Returns an array of the uniform type identifiers that are supported for image destinations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagedestinationgettypeid())*