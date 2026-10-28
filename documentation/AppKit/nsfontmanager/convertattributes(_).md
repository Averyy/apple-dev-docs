# convertAttributes(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Converts attributes in response to an object initiating an attribute change, typically the Font panel or Font menu.

**Availability**:
- macOS

## Declaration

```swift
func convertAttributes(_ attributes: [String : Any] = [:]) -> [String : Any]
```

```objc
- (NSDictionary<NSString *,id> *) convertAttributes:(NSDictionary<NSString *,id> *) attributes;
```

## Return Value

The converted attributes, or `attributes` itself if the conversion isn’t possible.

## Discussion

Attributes unused by the sender should not be changed or removed.

This method is usually invoked on the sender of [`changeAttributes(_:)`](../nstextview/changeattributes%28_%29.md). See [Working with the Font Manager](https://developer.apple.com/library/archive/documentation/TextFonts/Conceptual/CocoaTextArchitecture/FontHandling/FontHandling.html#//apple_ref/doc/uid/TP40009459-CH5-SW9) for more information.

## Parameters

- `attributes`: The current attributes.

## See Also

### Setting Attributes
- [func setSelectedAttributes([String : Any], isMultiple: Bool)](./setselectedattributes%28_,ismultiple%29.md)
  Informs the Font panel that the specified font attributes changed for the selected text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/convertattributes(_:))*