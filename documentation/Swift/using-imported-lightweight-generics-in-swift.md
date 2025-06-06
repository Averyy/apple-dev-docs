# Using Imported Lightweight Generics in Swift

**Framework**: Swift

Understand the constraints of imported Obj-C lightweight generic type declarations.

#### Overview

Objective-C type declarations that use lightweight generic parameterization are imported by Swift with information about the type of their contents preserved. For example, given the following Objective-C property declarations:

```occ
@property NSArray<NSDate *> *dates;
@property NSCache<NSObject *, id<NSDiscardableContent>> *cachedData;
@property NSDictionary <NSString *, NSArray<NSLocale *> *> *supportedLocales;
```

Here’s the Swift version of those declarations when you import them:

```swift
var dates: [Date]
var cachedData: NSCache<NSObject, NSDiscardableContent>
var supportedLocales: [String: [Locale]]
```

A parameterized class written in Objective-C is imported into Swift as a generic class with the same number of type parameters. All Objective-C generic type parameters imported by Swift have a type constraint that requires that type to be a class (`T: AnyObject`).

If the Objective-C generic parameterization specifies class or protocols qualifications, the imported Swift declaration has a constraint that requires that type to be a subclass of the specified class or to conform to the specified protocol. For an unspecialized Objective-C type, Swift infers the generic parameterization for the imported class type constraints. For example, consider the following Objective-C class and category declarations:

```occ
@interface List<T: id<NSCopying>> : NSObject
- (List<T> *)listByAppendingItemsInList:(List<T> *)otherList;
@end

@interface ListContainer : NSObject
- (List<NSValue *> *)listOfValues;
@end

@interface ListContainer (ObjectList)
- (List *)listOfObjects;
@end
```

When you import these declarations into Swift, the `NSCopying` protocol qualification of the `List` type and the `NSValue` class qualification of the `listOfValues` method are preserved. In addition, the unqualified `listOfObjects` method uses the `NSCopying` generic constraint inferred from the `List` type.

```swift
class List<T: NSCopying> : NSObject {
    func listByAppendingItemsInList(otherList: List<T>) -> List<T>
}

class ListContainer : NSObject {
    func listOfValues() -> List<NSValue>
}

extension ListContainer {
    func listOfObjects() -> List<NSCopying>
}
```

## See Also

- [Using Imported Protocol-Qualified Classes in Swift](using-imported-protocol-qualified-classes-in-swift.md)
  Learn how imported Objective-C protocol-qualified classes and metaclasses are represented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/using-imported-lightweight-generics-in-swift)*