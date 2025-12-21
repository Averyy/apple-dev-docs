# Designating Nullability in Objective-C APIs

**Framework**: Swift

Use nullability annotations or mark regions as annotated to control how Objective-C declarations are imported into Swift.

#### Overview

In Objective-C, you work with references to objects by using pointers that can be null, called `nil` in Objective-C. In Swift, all values — including object instances — are guaranteed to be non-null. Instead, you represent a value that could be missing as wrapped in an optional type. When you need to indicate that a value is missing, you use the value `nil`.

You can annotate declarations in your Objective-C code to indicate whether an instance can have a null or `nil` value. Those annotations change how Swift imports your declarations. For an example of how Swift imports unannotated declarations, consider the following code:

```occ
@interface MyList : NSObject
- (MyListItem *)itemWithName:(NSString *)name;
- (NSString *)nameForItem:(MyListItem *)item;
@property (copy) NSArray<MyListItem *> *allItems;
@end
```

Swift imports each object instance parameter, return value, and property as an implicitly wrapped optional:

```swift
class MyList: NSObject {
    func item(withName name: String!) -> MyListItem!
    func name(for item: MyListItem!) -> String!
    var allItems: [MyListItem]!
}
```

##### Annotate Nullability of Individual Declarations

You can use nullability annotations in your Objective-C code to designate whether a parameter type, property type, or return type is nullable. Annotate property declarations, parameter types, and return types that are simple objects or block pointers using the `nullable`, `nonnull`, and `null_resettable` property attributes. If no nullability information is provided for a type, Swift doesn’t distinguish between optional and nonoptional references, and imports the type as an implicitly unwrapped optional.

This list describes how Swift imports types with different nullability annotations:

- Nonnullable—Imported as nonoptionals, whether annotated directly or by inclusion in an annotated region
- Nullable—Imported as optionals
- Without a nullability annotation or with a null_resettable annotation—Imported as implicitly unwrapped optionals

The following code shows the `MyList` type after annotation. The return types of the two methods are annotated as `nullable`, because the methods return `nil` if the list doesn’t contain the given list item or name. All other object instances are annotated as `nonnull`.

```occ
@interface MyList : NSObject
- (nullable MyListItem *)itemWithName:(nonnull NSString *)name;
- (nullable NSString *)nameForItem:(nonnull MyListItem *)item;
@property (copy, nonnull) NSArray<MyListItem *> *allItems;
@end
```

With these annotations, Swift imports the `MyList` type without using any implicitly wrapped optionals:

```swift
class MyList: NSObject {
    func item(withName name: String) -> MyListItem?
    func name(for item: MyListItem) -> String?
    var allItems: [MyListItem]
}
```

The `nullable` and `nonnull` annotations are simplified forms of the `_Nullable` and `_Nonnull` annotations, which you can use in almost any context that you would use the `const` keyword with a pointer type. Complex pointer types, such as `id *`, must be explicitly annotated using these annotations. For example, to specify a nonnullable pointer to a nullable object reference, use `_Nullable id * _Nonnull`.

##### Annotate Regions As Nonnullable

You can simplify the process of annotating your Objective-C code by marking entire regions as audited for nullability. Within a section of code demarcated by the `NS_ASSUME_NONNULL_BEGIN` and `NS_ASSUME_NONNULL_END` macros, you only need to annotate the nullable type declarations. Unannotated declarations within the audited region are treated as nonnullable.

Marking the `MyList` declaration as audited for nullability reduces the number of annotations that are required. Swift imports the type the same way as in the previous section.

```occ
NS_ASSUME_NONNULL_BEGIN

@interface MyList : NSObject
- (nullable MyListItem *)itemWithName:(NSString *)name;
- (nullable NSString *)nameForItem:(MyListItem *)item;
@property (copy) NSArray<MyListItem *> *allItems;
@end

NS_ASSUME_NONNULL_END
```

Note that `typedef` types aren’t assumed to be nonnull, even within audited regions, because they aren’t inherently nullable.

## See Also

- [Renaming Objective-C APIs for Swift](renaming-objective-c-apis-for-swift.md)
  Use the `NS_SWIFT_NAME` macro to customize API names for Swift.
- [Improving Objective-C API Declarations for Swift](improving-objective-c-api-declarations-for-swift.md)
  Use the `NS_REFINED_FOR_SWIFT` macro to change how an API is imported into Swift.
- [Grouping Related Objective-C Constants](grouping-related-objective-c-constants.md)
  Add macros to your Objective-C types to group their values in Swift.
- [Marking API Availability in Objective-C](marking-api-availability-in-objective-c.md)
  Use a macro to denote the availability of an Objective-C API.
- [Making Objective-C APIs Unavailable in Swift](making-objective-c-apis-unavailable-in-swift.md)
  Use the `NS_SWIFT_UNAVAILABLE` macro to prevent an API from being used in Swift.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/designating-nullability-in-objective-c-apis)*