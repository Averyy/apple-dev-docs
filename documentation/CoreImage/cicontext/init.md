# init()

**Framework**: Core Image  
**Kind**: init

Initializes a context without a specific rendering destination, using default options.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
init()
```

#### Return Value

An initialized Core Image context.

#### Discussion

If you create a context without specifying a rendering destination, Core Image automatically chooses and internally manages a rendering destination based on the current device’s capabilities. You cannot use a context without an explicit destination for the methods listed in Drawing Images. Instead, use the methods listed in Rendering Images.

To specify additional options for the context, use the [`contextWithOptions:`](cicontext/contextwithoptions:.md) initializer instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/init())*