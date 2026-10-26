# NSDictionary

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A static collection of objects associated with unique keys.

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
class NSDictionary
```

```objc
@interface NSDictionary : NSObject
```

## Mentions

- [Implementing Handoff in Your App](./implementing-handoff-in-your-app.md)

#### Overview

You can use this type in Swift instead of a [`Dictionary`](../Swift/dictionary.md) in cases that require reference semantics.

The `NSDictionary` class declares the programmatic interface to objects that manage immutable associations of keys and values. For example, an interactive form could be represented as a dictionary, with the field names as keys, corresponding to user-entered values.

Use this class or its subclass [`NSMutableDictionary`](./nsmutabledictionary.md) when you need a convenient and efficient way to retrieve data associated with an arbitrary key. `NSDictionary` creates static dictionaries, and `NSMutableDictionary` creates dynamic dictionaries. (For convenience, the term *dictionary* refers to any instance of one of these classes without specifying its exact class membership.)

A key-value pair within a dictionary is called an entry. Each entry consists of one object that represents the key and a second object that is that key’s value. Within a dictionary, the keys are unique. That is, no two keys in a single dictionary are equal (as determined by [`isEqual(_:)`](../ObjectiveC/nsobjectprotocol/isequal%28_%29.md)). In general, a key can be any object (provided that it conforms to the `NSCopying` protocol—see below), but note that when using key-value coding the key must be a string (see [Accessing Object Properties](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/BasicPrinciples.html#//apple_ref/doc/uid/20002170)). Neither a key nor a value can be `nil`; if you need to represent a null value in a dictionary, you should use [`NSNull`](./nsnull.md).

`NSDictionary` is “toll-free bridged” with its Core Foundation counterpart, [`CFDictionary`](../CoreFoundation/cfdictionary.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

##### Creating NSDictionary Objects Using Dictionary Literals

In addition to the provided initializers, such as [`init(objects:forKeys:)`](./nsdictionary/init%28objects,forkeys%29.md), you can create an `NSDictionary` object using a *dictionary literal*.

**Swift**:

```swift
let dictionary: NSDictionary = [
    "anObject" : someObject,
    "helloString" : "Hello, World!",
    "magicNumber" : 42,
    "aValue" : someValue
]
```

**Objective-C**:

```objc
NSDictionary *dictionary = @{
       @"anObject" : someObject,
    @"helloString" : @"Hello, World!",
    @"magicNumber" : @42,
         @"aValue" : someValue
};
```

In Objective-C, the compiler generates code that makes an underlying call to the [`dictionaryWithObjects:forKeys:count:`](./nsdictionary/dictionarywithobjects_forkeys_count_.md) method.

```objc
id objects[] = { someObject, @"Hello, World!", @42, someValue };
id keys[] = { @"anObject", @"helloString", @"magicNumber", @"aValue" };
NSUInteger count = sizeof(objects) / sizeof(id);
NSDictionary *dictionary = [NSDictionary dictionaryWithObjects:objects
                                                       forKeys:keys
                                                         count:count];
```

Unlike [`dictionaryWithObjectsAndKeys:`](./nsdictionary/dictionarywithobjectsandkeys_.md) and other initializers, dictionary literals specify entries in key-value order. You should not terminate the list of objects with `nil` when using this literal syntax, and in fact `nil` is an invalid value. For more information about object literals in Objective-C, see [Working with Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/WorkingwithObjects/WorkingwithObjects.html#//apple_ref/doc/uid/TP40011210-CH4) in [Programming with Objective-C](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011210).

In Swift, the `NSDictionary` class conforms to the `DictionaryLiteralConvertible` protocol, which allows it to be initialized with dictionary literals. For more information about object literals in Swift, see [Literal Expression](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/Expressions.html#//apple_ref/doc/uid/TP40014097-CH32-ID390) in [The Swift Programming Language (Swift 4.1)](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/index.html#//apple_ref/doc/uid/TP40014097).

##### Accessing Values Using Subscripting

In addition to the provided instance methods, such as [`object(forKey:)`](./nsdictionary/object%28forkey%29.md), you can access `NSDictionary` values by their keys using *subscripting*.

**Swift**:

```swift
let value = dictionary["helloString"]
```

**Objective-C**:

```objc
id value = dictionary[@"helloString"];
```

##### Enumerating Entries Using for-in Loops

In addition to the provided instance methods, such as [`enumerateKeysAndObjects(_:)`](./nsdictionary/enumeratekeysandobjects%28_%29.md), you can enumerate `NSDictionary` entries using *for-in loops*.

**Swift**:

```swift
for (key, value) in dictionary {
    print("Value: \(value) for key: \(key)")
}
```

**Objective-C**:

```objc
for (NSString *key in dictionary) {
    id value = dictionary[key];
    NSLog(@"Value: %@ for key: %@", value, key);
}
```

In Objective-C, `NSDictionary` conforms to the [`NSFastEnumeration`](./nsfastenumeration.md) protocol.

In Swift, `NSDictionary` conforms to the `SequenceType` protocol.

##### Subclassing Notes

You generally shouldn’t need to subclass `NSDictionary`. Custom behavior can usually be achieved through composition rather than subclassing.

###### Methods to Override

If you do need to subclass `NSDictionary`, take into account that it is a [Class cluster](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassCluster.html#//apple_ref/doc/uid/TP40008195-CH7). Any subclass must override the following primitive methods:

- [`init(objects:forKeys:count:)`](./nsdictionary/init%28objects,forkeys,count%29.md)
- [`count`](./nsdictionary/count.md)
- [`object(forKey:)`](./nsdictionary/object%28forkey%29.md)
- [`keyEnumerator()`](./nsdictionary/keyenumerator%28%29.md)

The other methods of `NSDictionary` operate by invoking one or more of these primitives. The non-primitive methods provide convenient ways of accessing multiple entries at once.

###### Alternatives to Subclassing

Before making a custom class of `NSDictionary`, investigate [`NSMapTable`](./nsmaptable.md) and the corresponding Core Foundation type, [`CFDictionary`](../CoreFoundation/cfdictionary.md). Because `NSDictionary` and `CFDictionary` are “toll-free bridged,” you can substitute a `CFDictionary` object for a `NSDictionary` object in your code (with appropriate casting). Although they are corresponding types, `CFDictionary` and `NSDictionary` do not have identical interfaces or implementations, and you can sometimes do things with `CFDictionary` that you cannot easily do with `NSDictionary`.

If the behavior you want to add supplements that of the existing class, you could write a category on `NSDictionary`. Keep in mind, however, that this category will be in effect for all instances of `NSDictionary` that you use, and this might have unintended consequences. Alternatively, you could use composition to achieve the desired behavior.

## Topics

### Creating an Empty Dictionary
- [init()](./nsdictionary/init%28%29.md)
  Initializes a newly allocated dictionary.
- [+ dictionary](./nsdictionary/dictionary.md)
  Creates an empty dictionary.
### Creating a Dictionary from Objects and Keys
- [convenience init(objects: [Any], forKeys: [any NSCopying])](./nsdictionary/init%28objects,forkeys%29.md)
  Initializes a newly allocated dictionary with key-value pairs constructed from the provided arrays of keys and objects.
- [init(objects: UnsafePointer<AnyObject>?, forKeys: UnsafePointer<any NSCopying>?, count: Int)](./nsdictionary/init%28objects,forkeys,count%29.md)
  Initializes a newly allocated dictionary with the specified number of key-value pairs constructed from the provided C arrays of keys and objects.
- [convenience init(object: Any, forKey: any NSCopying)](./nsdictionary/init%28object,forkey%29.md)
  Creates a dictionary containing a given key and value.
- [+ dictionaryWithObjects:forKeys:](./nsdictionary/dictionarywithobjects_forkeys_.md)
  Creates a dictionary containing entries constructed from the contents of an array of keys and an array of values.
- [+ dictionaryWithObjects:forKeys:count:](./nsdictionary/dictionarywithobjects_forkeys_count_.md)
  Creates a dictionary containing a specified number of objects from a C array.
- [+ dictionaryWithObjectsAndKeys:](./nsdictionary/dictionarywithobjectsandkeys_.md)
  Creates a dictionary containing entries constructed from the specified set of values and keys.
- [- initWithObjectsAndKeys:](./nsdictionary/initwithobjectsandkeys_.md)
  Initializes a newly allocated dictionary with entries constructed from the specified set of values and keys.
### Creating a Dictionary from Another Dictionary
- [convenience init(dictionary: [AnyHashable : Any])](./nsdictionary/init%28dictionary%29-9fw1u.md)
  Initializes a newly allocated dictionary by placing in it the keys and values contained in another given dictionary.
- [convenience init(dictionary: [AnyHashable : Any], copyItems: Bool)](./nsdictionary/init%28dictionary,copyitems%29.md)
  Initializes a newly allocated dictionary using the objects contained in another given dictionary.
- [convenience init(dictionaryLiteral: (Any, Any)...)](./nsdictionary/init%28dictionaryliteral%29.md)
  Initializes a newly allocated dictionary from the given key-value pairs.
- [+ dictionaryWithDictionary:](./nsdictionary/dictionarywithdictionary_.md)
  Creates a dictionary containing the keys and values from another given dictionary.
### Creating a Dictionary from an External Source
- [convenience init(contentsOfURL: URL, error: ()) throws](./nsdictionary/init%28contentsofurl,error%29.md)
  Initializes a newly allocated dictionary using the keys and values found at a given URL.
- [convenience init?(contentsOfFile: String)](./nsdictionary/init%28contentsoffile%29.md)
  Initializes a newly allocated dictionary using the keys and values found in a file at a given path.
- [+ dictionaryWithContentsOfURL:error:](./nsdictionary/dictionarywithcontentsofurl_error_.md)
  Creates a dictionary using the keys and values found in a resource specified by a given URL.
- [+ dictionaryWithContentsOfFile:](./nsdictionary/dictionarywithcontentsoffile_.md)
  Creates a dictionary using the keys and values found in a file specified by a given path.
### Creating a Dictionary from an NSCoder
- [init?(coder: NSCoder)](./nsdictionary/init%28coder%29.md)
  Creates a dictionary initialized from data in the provided unarchiver.
### Creating Key Sets for Shared-Key Optimized Dictionaries
- [class func sharedKeySet(forKeys: [any NSCopying]) -> Any](./nsdictionary/sharedkeyset%28forkeys%29.md)
  Creates a shared key set object for the specified keys.
### Counting Entries
- [var count: Int](./nsdictionary/count.md)
  The number of entries in the dictionary.
### Comparing Dictionaries
- [func isEqual(to: [AnyHashable : Any]) -> Bool](./nsdictionary/isequal%28to%29.md)
  Returns a Boolean value that indicates whether the contents of the receiving dictionary are equal to the contents of another given dictionary.
### Accessing Keys and Values
- [var allKeys: [Any]](./nsdictionary/allkeys.md)
  A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [func allKeys(for: Any) -> [Any]](./nsdictionary/allkeys%28for%29.md)
  Returns a new array containing the keys corresponding to all occurrences of a given object in the dictionary.
- [var allValues: [Any]](./nsdictionary/allvalues.md)
  A new array containing the dictionary’s values, or an empty array if the dictionary has no entries.
- [func value(forKey: String) -> Any?](./nsdictionary/value%28forkey%29.md)
  Returns the value associated with a given key.
- [func objects(forKeys: [Any], notFoundMarker: Any) -> [Any]](./nsdictionary/objects%28forkeys,notfoundmarker%29.md)
  Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.
- [func object(forKey: Any) -> Any?](./nsdictionary/object%28forkey%29.md)
  Returns the value associated with a given key.
- [subscript(any NSCopying) -> Any?](./nsdictionary/subscript%28_%29-52n56.md)
  Returns the value associated with a given key.
- [subscript(Any) -> Any?](./nsdictionary/subscript%28_%29-1bt1b.md)
  Accesses the value associated with a given key.
- [- getObjects:andKeys:count:](./nsdictionary/getobjects_andkeys_count_.md)
  Returns by reference C arrays of the keys and values in the dictionary.
- [- getObjects:andKeys:](./nsdictionary/getobjects_andkeys_.md)
  Returns by reference C arrays of the keys and values in the dictionary.
### Enumerating Dictionaries
- [func keyEnumerator() -> NSEnumerator](./nsdictionary/keyenumerator%28%29.md)
  Provides an enumerator to access the keys in the dictionary.
- [func objectEnumerator() -> NSEnumerator](./nsdictionary/objectenumerator%28%29.md)
  Returns an enumerator object that lets you access each value in the dictionary.
- [func enumerateKeysAndObjects((Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./nsdictionary/enumeratekeysandobjects%28_%29.md)
  Applies a given block object to the entries of the dictionary.
- [func enumerateKeysAndObjects(options: NSEnumerationOptions, using: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./nsdictionary/enumeratekeysandobjects%28options,using%29.md)
  Applies a given block object to the entries of the dictionary, with options specifying how the enumeration is performed.
- [func makeIterator() -> NSDictionary.Iterator](./nsdictionary/makeiterator%28%29.md)
  Returns an iterator over the elements of this sequence.
- [- countByEnumeratingWithState:objects:count:](./nsdictionary/countbyenumeratingwithstate_objects_count_.md)
  Returns by reference a C array of objects over which the sender should iterate.
### Sorting Dictionaries
- [func keysSortedByValue(using: Selector) -> [Any]](./nsdictionary/keyssortedbyvalue%28using%29.md)
  Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values.
- [func keysSortedByValue(comparator: (Any, Any) -> ComparisonResult) -> [Any]](./nsdictionary/keyssortedbyvalue%28comparator%29.md)
  Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block.
- [func keysSortedByValue(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult) -> [Any]](./nsdictionary/keyssortedbyvalue%28options,usingcomparator%29.md)
  Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block and a specified set of options.
### Filtering Dictionaries
- [func keysOfEntries(passingTest: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](./nsdictionary/keysofentries%28passingtest%29.md)
  Returns the set of keys whose corresponding value satisfies a constraint described by a block object.
- [func keysOfEntries(options: NSEnumerationOptions, passingTest: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](./nsdictionary/keysofentries%28options,passingtest%29.md)
  Returns the set of keys whose corresponding value satisfies a constraint described by a block object.
### Storing Dictionaries
- [func write(to: URL) throws](./nsdictionary/write%28to%29.md)
  Writes a property list representation of the contents of the dictionary to a given URL.
- [func write(to: URL, atomically: Bool) -> Bool](./nsdictionary/write%28to,atomically%29.md)
  Writes a property list representation of the contents of the dictionary to a given URL.
- [func write(toFile: String, atomically: Bool) -> Bool](./nsdictionary/write%28tofile,atomically%29.md)
  Writes a property list representation of the contents of the dictionary to a given path.
### Accessing File Attributes
- [func fileSize() -> UInt64](./nsdictionary/filesize%28%29.md)
  Returns the file’s size, in bytes.
- [func fileType() -> String?](./nsdictionary/filetype%28%29.md)
  Returns the file type.
- [func fileCreationDate() -> Date?](./nsdictionary/filecreationdate%28%29.md)
  Returns the file’s creation date.
- [func fileModificationDate() -> Date?](./nsdictionary/filemodificationdate%28%29.md)
  Returns file’s modification date.
- [func filePosixPermissions() -> Int](./nsdictionary/fileposixpermissions%28%29.md)
  Returns the file’s POSIX permissions.
- [func fileOwnerAccountID() -> NSNumber?](./nsdictionary/fileowneraccountid%28%29.md)
  Returns the file’s owner account ID.
- [func fileOwnerAccountName() -> String?](./nsdictionary/fileowneraccountname%28%29.md)
  Returns the file’s owner account name.
- [func fileGroupOwnerAccountID() -> NSNumber?](./nsdictionary/filegroupowneraccountid%28%29.md)
  Returns file’s group owner account ID.
- [func fileGroupOwnerAccountName() -> String?](./nsdictionary/filegroupowneraccountname%28%29.md)
  Returns the file’s group owner account name.
- [func fileExtensionHidden() -> Bool](./nsdictionary/fileextensionhidden%28%29.md)
  Returns a Boolean value indicating whether the file hides its extension.
- [func fileIsImmutable() -> Bool](./nsdictionary/fileisimmutable%28%29.md)
  Returns a Boolean value indicating whether the file is immutable.
- [func fileIsAppendOnly() -> Bool](./nsdictionary/fileisappendonly%28%29.md)
  Returns a Boolean value indicating whether the file is append only.
- [func fileSystemFileNumber() -> Int](./nsdictionary/filesystemfilenumber%28%29.md)
  Returns the filesystem file number.
- [func fileSystemNumber() -> Int](./nsdictionary/filesystemnumber%28%29.md)
  Returns the filesystem number.
- [func fileHFSTypeCode() -> OSType](./nsdictionary/filehfstypecode%28%29.md)
  Returns file’s HFS type code.
- [func fileHFSCreatorCode() -> OSType](./nsdictionary/filehfscreatorcode%28%29.md)
  Returns the file’s HFS creator code.
### Describing a Dictionary
- [var description: String](./nsdictionary/description.md)
  A string that represents the contents of the dictionary, formatted as a property list.
- [var descriptionInStringsFileFormat: String](./nsdictionary/descriptioninstringsfileformat.md)
  A string that represents the contents of the dictionary, formatted in `.strings` file format.
- [func description(withLocale: Any?) -> String](./nsdictionary/description%28withlocale%29.md)
  Returns a string object that represents the contents of the dictionary, formatted as a property list.
- [func description(withLocale: Any?, indent: Int) -> String](./nsdictionary/description%28withlocale,indent%29.md)
  Returns a string object that represents the contents of the dictionary, formatted as a property list.
### Supporting Types
- [NSDictionary.Iterator](./nsdictionary/iterator.md)
  A class that you use to provide members of a dictionary, one-by-one.
### Initializers
- [convenience init?(contentsOf: URL)](./nsdictionary/init%28contentsof%29.md)
  Initializes a newly allocated dictionary using the keys and values found at a given URL.
- [convenience init(contentsOf: URL, error: ()) throws](./nsdictionary/init%28contentsof,error%29.md)
  Initializes a newly allocated dictionary using the keys and values found at a given URL.
- [convenience init(dictionary: NSDictionary)](./nsdictionary/init%28dictionary%29-4gc13.md)
  Initializes a newly allocated dictionary and adds to it objects from another given dictionary.
### Default Implementations
- [ExpressibleByDictionaryLiteral Implementations](./nsdictionary/expressiblebydictionaryliteral-implementations.md)
- [NSDictionary Implementations](./nsdictionary/nsdictionary-implementations.md)
- [Sequence Implementations](./nsdictionary/sequence-implementations.md)
### Type Methods
- [+ dictionaryWithContentsOfURL:](./nsdictionary/dictionarywithcontentsofurl_.md)
  Creates a dictionary using the keys and values found in a resource specified by a given URL.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NSMutableDictionary](./nsmutabledictionary.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByDictionaryLiteral](../Swift/expressiblebydictionaryliteral.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSFastEnumeration](./nsfastenumeration.md)
- [NSFetchRequestResult](../CoreData/nsfetchrequestresult.md)
- [NSMutableCopying](./nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Basic Collections
- [NSArray](./nsarray.md)
  A static ordered collection of objects.
- [NSMutableArray](./nsmutablearray.md)
  A dynamic ordered collection of objects.
- [NSMutableDictionary](./nsmutabledictionary.md)
  A dynamic collection of objects associated with unique keys.
- [NSSet](./nsset.md)
  A static, unordered collection of unique objects.
- [NSMutableSet](./nsmutableset.md)
  A dynamic unordered collection of unique objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary)*