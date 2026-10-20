# init(object:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates and returns an array containing a given object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(object anObject: Any)
```

```objc
+ (instancetype) arrayWithObject:(ObjectType) anObject;
```

#### Return Value

An array containing the single element `anObject`.

#### Discussion

Alternatively, you can use array literal syntax in Objective-C or Swift to create an array containing a given object:

**Swift**:

```swift
let array: NSArray = ["Hello, world!"]
```

**Objective-C**:

```objc
NSArray *array = @[@"Hello, world!"];
```

## Parameters

- `anObject`: An object.

## See Also

### Creating an Array
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](./init%28objects,count%29-7dct1.md)
  Creates and returns an array that includes a given number of objects from a given C array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/init(object:))*