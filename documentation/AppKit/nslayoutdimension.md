# NSLayoutDimension

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A factory class for creating size-based layout constraint objects using a fluent API.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class NSLayoutDimension
```

```objc
@interface NSLayoutDimension : NSLayoutAnchor
```

## Overview

Use these constraints to programmatically define your layout using Auto Layout. All sizes are measured in points. In addition to providing size-specific methods for creating constraints, this class adds type information to the methods inherited from [`NSLayoutAnchor`](./nslayoutanchor.md). Specifically, the generic methods declared by [`NSLayoutAnchor`](./nslayoutanchor.md) must now take a matching [`NSLayoutDimension`](./nslayoutdimension.md) object.

**Swift**:

```swift
// This code works as expected.
saveButton.widthAnchor.constraint(equalTo: cancelButton.widthAnchor).isActive = true

// This code generates an incompatible pointer type warning.
saveButton.widthAnchor.constraint(equalTo: cancelButton.leadingAnchor).isActive = true
```

**Objective-C**:

```objc
// This code works as expected.
[self.saveButton.widthAnchor constraintEqualToAnchor:self.cancelButton.widthAnchor].active = YES;
 
// This code generates an incompatible pointer type warning.
[self.saveButton.widthAnchor constraintEqualToAnchor:self.cancelButton.leadingAnchor].active = YES;
```

For more information on using layout anchors, see [`NSLayoutAnchor`](./nslayoutanchor.md).

## Topics

### Building constraints
- [func constraint(equalTo: NSLayoutDimension, multiplier: CGFloat) -> NSLayoutConstraint](./nslayoutdimension/constraint%28equalto,multiplier%29.md)
  Returns a constraint that defines the anchor’s size attribute as equal to the specified anchor multiplied by the constant.
- [func constraint(equalTo: NSLayoutDimension, multiplier: CGFloat, constant: CGFloat) -> NSLayoutConstraint](./nslayoutdimension/constraint%28equalto,multiplier,constant%29.md)
  Returns a constraint that defines the anchor’s size attribute as equal to the specified size attribute multiplied by a constant plus an offset.
- [func constraint(equalToConstant: CGFloat) -> NSLayoutConstraint](./nslayoutdimension/constraint%28equaltoconstant%29.md)
  Returns a constraint that defines a constant size for the anchor’s size attribute.
- [func constraint(greaterThanOrEqualTo: NSLayoutDimension, multiplier: CGFloat) -> NSLayoutConstraint](./nslayoutdimension/constraint%28greaterthanorequalto,multiplier%29.md)
  Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant.
- [func constraint(greaterThanOrEqualTo: NSLayoutDimension, multiplier: CGFloat, constant: CGFloat) -> NSLayoutConstraint](./nslayoutdimension/constraint%28greaterthanorequalto,multiplier,constant%29.md)
  Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant plus an offset.
- [func constraint(greaterThanOrEqualToConstant: CGFloat) -> NSLayoutConstraint](./nslayoutdimension/constraint%28greaterthanorequaltoconstant%29.md)
  Returns a constraint that defines the minimum size for the anchor’s size attribute.
- [func constraint(lessThanOrEqualTo: NSLayoutDimension, multiplier: CGFloat) -> NSLayoutConstraint](./nslayoutdimension/constraint%28lessthanorequalto,multiplier%29.md)
  Returns a constraint that defines the anchor’s size attribute as less than or equal to the specified anchor multiplied by the constant.
- [func constraint(lessThanOrEqualTo: NSLayoutDimension, multiplier: CGFloat, constant: CGFloat) -> NSLayoutConstraint](./nslayoutdimension/constraint%28lessthanorequalto,multiplier,constant%29.md)
  Returns a constraint that defines the anchor’s size attribute as greater than or equal to the specified anchor multiplied by the constant plus an offset.
- [func constraint(lessThanOrEqualToConstant: CGFloat) -> NSLayoutConstraint](./nslayoutdimension/constraint%28lessthanorequaltoconstant%29.md)
  Returns a constraint that defines the maximum size for the anchor’s size attribute.

## Relationships

### Inherits From
- [NSLayoutAnchor](./nslayoutanchor.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Layout Guides
- [class NSLayoutGuide](./nslayoutguide.md)
  A rectangular area that can interact with Auto Layout.
- [NSViewLayoutRegion](./nsviewlayoutregion.md)
- [NSViewLayoutRegionAdaptivityAxis](./nsviewlayoutregionadaptivityaxis.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutdimension)*