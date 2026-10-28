# BEAccessibilityTextMarker

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

An abstract class that represents a location in an element’s accessibility text.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- macOS
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
class BEAccessibilityTextMarker
```

```objc
@interface BEAccessibilityTextMarker : NSObject
```

## Overview

Subclass `BEAccessibilityTextMarker` in your app to represent a location in the accessibility text of an element in the document object model (DOM). The system uses your implementation of [`BEAccessibilityTextMarkerSupport`](./beaccessibilitytextmarkersupport.md) to convert between accessibility text markers and locations in your app’s views, and doesn’t create instances of your subclass or access their data.

## Topics

### Initializers
- [init?(coder: NSCoder)](./beaccessibilitytextmarker/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Text positions
- [func accessibilityNextTextMarker(BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](./beaccessibilitytextmarkersupport/accessibilitynexttextmarker%28_%29.md)
  Returns the text marker that follows the given text marker.
- [func accessibilityPreviousTextMarker(BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](./beaccessibilitytextmarkersupport/accessibilityprevioustextmarker%28_%29.md)
  Returns the text marker that precedes the given text marker.
- [func accessibilityLineStartMarker(for: BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](./beaccessibilitytextmarkersupport/accessibilitylinestartmarker%28for%29.md)
  Returns the text marker that represents the start of the line that contains the given text marker.
- [func accessibilityLineEndMarker(for: BEAccessibilityTextMarker) -> BEAccessibilityTextMarker?](./beaccessibilitytextmarkersupport/accessibilitylineendmarker%28for%29.md)
  Returns the text marker that represents the end of the line that contains the given text marker.
- [func accessibilityMarker(for: CGPoint) -> BEAccessibilityTextMarker?](./beaccessibilitytextmarkersupport/accessibilitymarker%28for%29.md)
  Returns the text marker at a point in the view’s coordinate system.
- [func accessibilityTextMarker(forPosition: Int) -> BEAccessibilityTextMarker?](./beaccessibilitytextmarkersupport/accessibilitytextmarker%28forposition%29.md)
  Returns the text marker for the text at a given index in the element’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilitytextmarker)*