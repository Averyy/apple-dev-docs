# init(info:domainDimension:domain:rangeDimension:range:callbacks:)

**Framework**: Core Graphics  
**Kind**: init

Creates a Core Graphics function.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(info: UnsafeMutableRawPointer?, domainDimension: Int, domain: UnsafePointer<CGFloat>?, rangeDimension: Int, range: UnsafePointer<CGFloat>?, callbacks: UnsafePointer<CGFunctionCallbacks>)
```

#### Return Value

The new Core Graphics function. In Objective-C, you’re responsible for releasing this object using [`CGFunctionRelease`](cgfunctionrelease.md).

## Parameters

- `info`: A pointer to user-defined storage for data that you want to pass to your callbacks. You need to make sure that the data persists for as long as it’s needed, which can be beyond the scope in which the Core Graphics function is used.
- `domainDimension`: The number of inputs.
- `domain`: An array of ( ) floats used to specify the valid intervals of input values. For each k from   to  ,   must be less than or equal to  , and the  th input value will be clipped to lie in the interval  . If this parameter is  , then the input values are not clipped.
- `rangeDimension`: The number of outputs.
- `range`: An array of   floats that specifies the valid intervals of output values. For each   from   to  ,   must be less than or equal to  , and the  th output value will be clipped to lie in the interval  . 	If this parameter is  , then the output values are not clipped.
- `callbacks`: A pointer to a callback function table. This table should contain pointers to the callbacks you provide to implement the semantics of this Core Graphics function.	 Core Graphics makes a copy of your table, so, for example, you could safely pass in a pointer to a structure on the stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfunction/init(info:domaindimension:domain:rangedimension:range:callbacks:))*