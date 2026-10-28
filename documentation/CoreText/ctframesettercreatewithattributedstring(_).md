# CTFramesetterCreateWithAttributedString(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Creates an immutable framesetter object from an attributed string.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTFramesetterCreateWithAttributedString(_ attrString: CFAttributedString) -> CTFramesetter
```

```c
extern CTFramesetterRefCTFramesetterCreateWithAttributedString(CFAttributedStringRef attrString);
```

## Return Value

A reference to a framesetter object if the call is successful; otherwise, `NULL`.

## Discussion

Use the framesetter object to create and fill text frames with the [`CTFramesetterCreateFrame(_:_:_:_:)`](./ctframesettercreateframe%28_,_,_,_%29.md) call.

> **Note**:  By default, the text system doesn’t typeset text that requires an unreasonable amount of effort. To create a framesetter that supports typesetting text regardless of the amount of effort necessary, create a [`CTTypesetter`](./cttypesetter.md) with the [`kCTTypesetterOptionAllowUnboundedLayout`](./kcttypesetteroptionallowunboundedlayout.md) option set to [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md), then use [`CTFramesetterCreateWithTypesetter(_:)`](./ctframesettercreatewithtypesetter%28_%29.md) instead.

## Parameters

- `attrString`: The attributed string for constructing the framesetter object.

## See Also

### Creating a Framesetter
- [func CTFramesetterCreateWithTypesetter(CTTypesetter) -> CTFramesetter](./ctframesettercreatewithtypesetter%28_%29.md)
  Creates a framesetter directly from a typesetter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctframesettercreatewithattributedstring(_:))*