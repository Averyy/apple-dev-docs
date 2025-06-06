# offset(of:)

**Framework**: Swift  
**Kind**: method

Returns the offset of an inline stored property within a type’s in-memory representation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static func offset(of key: PartialKeyPath<T>) -> Int?
```

#### Return Value

The offset in bytes from a pointer to a value of type `T` to a pointer to the storage referenced by `key`, or `nil` if no such offset is available for the storage referenced by `key`. If the value is `nil`, it can be because `key` is computed, has observers, requires reabstraction, or overlaps storage with other properties.

#### Discussion

You can use this method to find the distance in bytes that can be added to a pointer of type `T` to get a pointer to the property referenced by `key`. The offset is available only if the given key refers to inline, directly addressable storage within the in-memory representation of `T`.

If the return value of this method is non-`nil`, then accessing the value by key path or by an offset pointer are equivalent. For example, for a variable `root` of type `T`, a key path `key` of type `WritableKeyPath<T, U>`, and a `value` of type `U`:

```swift
// Mutation through the key path
root[keyPath: key] = value

// Mutation through the offset pointer
withUnsafeMutableBytes(of: &root) { bytes in
    let offset = MemoryLayout<T>.offset(of: key)!
    let rawPointerToValue = bytes.baseAddress! + offset
    let pointerToValue = rawPointerToValue.assumingMemoryBound(to: U.self)
    pointerToValue.pointee = value
}
```

A property has inline, directly addressable storage when it is a stored property for which no additional work is required to extract or set the value. Properties are not directly accessible if they trigger any `didSet` or `willSet` accessors, perform any representation changes such as bridging or closure reabstraction, or mask the value out of overlapping storage as for packed bitfields. In addition, because class instance properties are always stored out-of-line, their positions are not accessible using `offset(of:)`.

For example, in the `ProductCategory` type defined here, only `\.updateCounter`, `\.identifier`, and `\.identifier.name` refer to properties with inline, directly addressable storage:

```swift
struct ProductCategory {
    struct Identifier {
        var name: String              // addressable
    }

    var identifier: Identifier        // addressable
    var updateCounter: Int            // addressable
    var products: [Product] {         // not addressable: didSet handler
        didSet { updateCounter += 1 }
    }
    var productCount: Int {           // not addressable: computed property
        return products.count
    }
}
```

When using `offset(of:)` with a type imported from a library, don’t assume that future versions of the library will have the same behavior. If a property is converted from a stored property to a computed property, the result of `offset(of:)` changes to `nil`. That kind of conversion is nonbreaking in other contexts, but would trigger a runtime error if the result of `offset(of:)` is force-unwrapped.

## Parameters

- `key`: A key path referring to storage that can be accessed   through a value of type  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/memorylayout/offset(of:))*