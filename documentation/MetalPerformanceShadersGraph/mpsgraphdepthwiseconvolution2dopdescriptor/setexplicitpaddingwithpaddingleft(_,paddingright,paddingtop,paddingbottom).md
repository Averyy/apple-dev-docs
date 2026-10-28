# setExplicitPaddingWithPaddingLeft(_:paddingRight:paddingTop:paddingBottom:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method  
**Role**: Instance Method

Sets the explicit padding values.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func setExplicitPaddingWithPaddingLeft(_ paddingLeft: Int, paddingRight: Int, paddingTop: Int, paddingBottom: Int)
```

```objc
- (void) setExplicitPaddingWithPaddingLeft:(NSUInteger) paddingLeft paddingRight:(NSUInteger) paddingRight paddingTop:(NSUInteger) paddingTop paddingBottom:(NSUInteger) paddingBottom;
```

## Discussion

Note: this method also sets `paddingStyle` to `MPSGraphPaddingStyleExplicit` (see [`MPSGraphPaddingStyle`](../mpsgraphpaddingstyle.md)).

## Parameters

- `paddingLeft`: See `paddingLeft` property.
- `paddingRight`: See `paddingRight` property.
- `paddingTop`: See `paddingTop` property.
- `paddingBottom`: See `paddingBottom` property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphdepthwiseconvolution2dopdescriptor/setexplicitpaddingwithpaddingleft(_:paddingright:paddingtop:paddingbottom:))*