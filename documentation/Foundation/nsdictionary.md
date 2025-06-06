# NSDictionary

**Framework**: Foundation  
**Kind**: class

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

## Mentions

- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md)

#### Overview

You can use this type in Swift instead of a [`Dictionary`](https://developer.apple.com/documentation/Swift/Dictionary) in cases that require reference semantics.

The `NSDictionary` class declares the programmatic interface to objects that manage immutable associations of keys and values. For example, an interactive form could be represented as a dictionary, with the field names as keys, corresponding to user-entered values.

Use this class or its subclass [`NSMutableDictionary`](nsmutabledictionary.md) when you need a convenient and efficient way to retrieve data associated with an arbitrary key. `NSDictionary` creates static dictionaries, and `NSMutableDictionary` creates dynamic dictionaries. (For convenience, the term  refers to any instance of one of these classes without specifying its exact class membership.)

A key-value pair within a dictionary is called an entry. Each entry consists of one object that represents the key and a second object that is that key’s value. Within a dictionary, the keys are unique. That is, no two keys in a single dictionary are equal (as determined by [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:))). In general, a key can be any object (provided that it conforms to the `NSCopying` protocol—see below), but note that when using key-value coding the key must be a string (see [`Accessing Object Properties`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/BasicPrinciples.html#//apple_ref/doc/uid/20002170)). Neither a key nor a value can be `nil`; if you need to represent a null value in a dictionary, you should use [`NSNull`](nsnull.md).

`NSDictionary` is “toll-free bridged” with its Core Foundation counterpart, [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary). See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

##### Creating Nsdictionary Objects Using Dictionary Literals

In addition to the provided initializers, such as [`init(objects:forKeys:)`](nsdictionary/init(objects:forkeys:).md), you can create an `NSDictionary` object using a .

In Objective-C, the compiler generates code that makes an underlying call to the [`dictionaryWithObjects:forKeys:count:`](nsdictionary/dictionarywithobjects:forkeys:count:.md) method.

```objc
id objects[] = { someObject, @"Hello, World!", @42, someValue };
id keys[] = { @"anObject", @"helloString", @"magicNumber", @"aValue" };
NSUInteger count = sizeof(objects) / sizeof(id);
NSDictionary *dictionary = [NSDictionary dictionaryWithObjects:objects
                                                       forKeys:keys
                                                         count:count];
```

Unlike [`dictionaryWithObjectsAndKeys:`](nsdictionary/dictionarywithobjectsandkeys:.md) and other initializers, dictionary literals specify entries in key-value order. You should not terminate the list of objects with `nil` when using this literal syntax, and in fact `nil` is an invalid value. For more information about object literals in Objective-C, see [`Working with Objects`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/WorkingwithObjects/WorkingwithObjects.html#//apple_ref/doc/uid/TP40011210-CH4) in [`Programming with Objective-C`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011210).

In Swift, the `NSDictionary` class conforms to the `DictionaryLiteralConvertible` protocol, which allows it to be initialized with dictionary literals. For more information about object literals in Swift, see [`Literal Expression`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/Expressions.html#//apple_ref/doc/uid/TP40014097-CH32-ID390) in [`The Swift Programming Language (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/index.html#//apple_ref/doc/uid/TP40014097).

##### Accessing Values Using Subscripting

In addition to the provided instance methods, such as [`object(forKey:)`](nsdictionary/object(forkey:).md), you can access `NSDictionary` values by their keys using .

##### Enumerating Entries Using for in Loops

In addition to the provided instance methods, such as [`enumerateKeysAndObjects(_:)`](nsdictionary/enumeratekeysandobjects(_:).md), you can enumerate `NSDictionary` entries using .

In Objective-C, `NSDictionary` conforms to the [`NSFastEnumeration`](nsfastenumeration.md) protocol.

In Swift, `NSDictionary` conforms to the `SequenceType` protocol.

##### Subclassing Notes

You generally shouldn’t need to subclass `NSDictionary`. Custom behavior can usually be achieved through composition rather than subclassing.

###### Methods to Override

If you do need to subclass `NSDictionary`, take into account that it is a [`Class cluster`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassCluster.html#//apple_ref/doc/uid/TP40008195-CH7). Any subclass must override the following primitive methods:

- [`init(objects:forKeys:count:)`](nsdictionary/init(objects:forkeys:count:).md)
- [`count`](nsdictionary/count.md)
- [`object(forKey:)`](nsdictionary/object(forkey:).md)
- [`keyEnumerator()`](nsdictionary/keyenumerator().md)

The other methods of `NSDictionary` operate by invoking one or more of these primitives. The non-primitive methods provide convenient ways of accessing multiple entries at once.

###### Alternatives to Subclassing

Before making a custom class of `NSDictionary`, investigate [`NSMapTable`](nsmaptable.md) and the corresponding Core Foundation type, [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary). Because `NSDictionary` and `CFDictionary` are “toll-free bridged,” you can substitute a `CFDictionary` object for a `NSDictionary` object in your code (with appropriate casting). Although they are corresponding types, `CFDictionary` and `NSDictionary` do not have identical interfaces or implementations, and you can sometimes do things with `CFDictionary` that you cannot easily do with `NSDictionary`.

If the behavior you want to add supplements that of the existing class, you could write a category on `NSDictionary`. Keep in mind, however, that this category will be in effect for all instances of `NSDictionary` that you use, and this might have unintended consequences. Alternatively, you could use composition to achieve the desired behavior.

## Topics

### Creating an Empty Dictionary
- [init()](nsdictionary/init.md)
  Initializes a newly allocated dictionary.
### Creating a Dictionary from Objects and Keys
- [convenience init(objects: [Any], forKeys: [any NSCopying])](nsdictionary/init(objects:forkeys:).md)
  Initializes a newly allocated dictionary with key-value pairs constructed from the provided arrays of keys and objects.
- [init(objects: UnsafePointer<AnyObject>?, forKeys: UnsafePointer<any NSCopying>?, count: Int)](nsdictionary/init(objects:forkeys:count:).md)
  Initializes a newly allocated dictionary with the specified number of key-value pairs constructed from the provided C arrays of keys and objects.
- [convenience init(object: Any, forKey: any NSCopying)](nsdictionary/init(object:forkey:).md)
  Creates a dictionary containing a given key and value.
### Creating a Dictionary from Another Dictionary
- [convenience init(dictionary: [AnyHashable : Any])](nsdictionary/init(dictionary:)-9fw1u.md)
  Initializes a newly allocated dictionary by placing in it the keys and values contained in another given dictionary.
- [convenience init(dictionary: [AnyHashable : Any], copyItems: Bool)](nsdictionary/init(dictionary:copyitems:).md)
  Initializes a newly allocated dictionary using the objects contained in another given dictionary.
### Creating a Dictionary from an External Source
- [init?(contentsOfURL: URL)](nsdictionary/init(contentsofurl:)-98pl3.md)
  Creates a dictionary using the keys and values found in a resource specified by a given URL.
- [convenience init(contentsOfURL: URL, error: ()) throws](nsdictionary/init(contentsofurl:error:).md)
  Initializes a newly allocated dictionary using the keys and values found at a given URL.
- [convenience init?(contentsOfURL: URL)](nsdictionary/init(contentsofurl:)-4pv16.md)
  Initializes a newly allocated dictionary using the keys and values found at a given URL.
- [convenience init?(contentsOfFile: String)](nsdictionary/init(contentsoffile:).md)
  Initializes a newly allocated dictionary using the keys and values found in a file at a given path.
### Creating a Dictionary from an NSCoder
- [init?(coder: NSCoder)](nsdictionary/init(coder:).md)
  Creates a dictionary initialized from data in the provided unarchiver.
### Creating Key Sets for Shared-Key Optimized Dictionaries
- [class func sharedKeySet(forKeys: [any NSCopying]) -> Any](nsdictionary/sharedkeyset(forkeys:).md)
  Creates a shared key set object for the specified keys.
### Counting Entries
- [var count: Int](nsdictionary/count.md)
  The number of entries in the dictionary.
### Comparing Dictionaries
- [func isEqual(to: [AnyHashable : Any]) -> Bool](nsdictionary/isequal(to:).md)
  Returns a Boolean value that indicates whether the contents of the receiving dictionary are equal to the contents of another given dictionary.
### Accessing Keys and Values
- [var allKeys: [Any]](nsdictionary/allkeys.md)
  A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [func allKeys(for: Any) -> [Any]](nsdictionary/allkeys(for:).md)
  Returns a new array containing the keys corresponding to all occurrences of a given object in the dictionary.
- [var allValues: [Any]](nsdictionary/allvalues.md)
  A new array containing the dictionary’s values, or an empty array if the dictionary has no entries.
- [func value(forKey: String) -> Any?](nsdictionary/value(forkey:).md)
  Returns the value associated with a given key.
- [func objects(forKeys: [Any], notFoundMarker: Any) -> [Any]](nsdictionary/objects(forkeys:notfoundmarker:).md)
  Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.
- [func object(forKey: Any) -> Any?](nsdictionary/object(forkey:).md)
  Returns the value associated with a given key.
- [subscript(any NSCopying) -> Any?](nsdictionary/subscript(_:)-52n56.md)
  Returns the value associated with a given key.
- [subscript(Any) -> Any?](nsdictionary/subscript(_:)-1bt1b.md)
  Accesses the value associated with a given key.
### Enumerating Dictionaries
- [func keyEnumerator() -> NSEnumerator](nsdictionary/keyenumerator.md)
  Provides an enumerator to access the keys in the dictionary.
- [func objectEnumerator() -> NSEnumerator](nsdictionary/objectenumerator.md)
  Returns an enumerator object that lets you access each value in the dictionary.
- [func enumerateKeysAndObjects((Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](nsdictionary/enumeratekeysandobjects(_:).md)
  Applies a given block object to the entries of the dictionary.
- [func enumerateKeysAndObjects(options: NSEnumerationOptions, using: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](nsdictionary/enumeratekeysandobjects(options:using:).md)
  Applies a given block object to the entries of the dictionary, with options specifying how the enumeration is performed.
- [func makeIterator() -> NSDictionary.Iterator](nsdictionary/makeiterator.md)
  Returns an iterator over the elements of this sequence.
### Sorting Dictionaries
- [func keysSortedByValue(using: Selector) -> [Any]](nsdictionary/keyssortedbyvalue(using:).md)
  Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values.
- [func keysSortedByValue(comparator: (Any, Any) -> ComparisonResult) -> [Any]](nsdictionary/keyssortedbyvalue(comparator:).md)
  Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block.
- [func keysSortedByValue(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult) -> [Any]](nsdictionary/keyssortedbyvalue(options:usingcomparator:).md)
  Returns an array of the dictionary’s keys, in the order they would be in if the dictionary were sorted by its values using a given comparator block and a specified set of options.
### Filtering Dictionaries
- [func keysOfEntries(passingTest: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](nsdictionary/keysofentries(passingtest:).md)
  Returns the set of keys whose corresponding value satisfies a constraint described by a block object.
- [func keysOfEntries(options: NSEnumerationOptions, passingTest: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](nsdictionary/keysofentries(options:passingtest:).md)
  Returns the set of keys whose corresponding value satisfies a constraint described by a block object.
### Storing Dictionaries
- [func write(to: URL) throws](nsdictionary/write(to:).md)
  Writes a property list representation of the contents of the dictionary to a given URL.
- [func write(to: URL, atomically: Bool) -> Bool](nsdictionary/write(to:atomically:).md)
  Writes a property list representation of the contents of the dictionary to a given URL.
- [func write(toFile: String, atomically: Bool) -> Bool](nsdictionary/write(tofile:atomically:).md)
  Writes a property list representation of the contents of the dictionary to a given path.
### Accessing File Attributes
- [func fileSize() -> UInt64](nsdictionary/filesize.md)
  Returns the file’s size, in bytes.
- [func fileType() -> String?](nsdictionary/filetype.md)
  Returns the file type.
- [func fileCreationDate() -> Date?](nsdictionary/filecreationdate.md)
  Returns the file’s creation date.
- [func fileModificationDate() -> Date?](nsdictionary/filemodificationdate.md)
  Returns file’s modification date.
- [func filePosixPermissions() -> Int](nsdictionary/fileposixpermissions.md)
  Returns the file’s POSIX permissions.
- [func fileOwnerAccountID() -> NSNumber?](nsdictionary/fileowneraccountid.md)
  Returns the file’s owner account ID.
- [func fileOwnerAccountName() -> String?](nsdictionary/fileowneraccountname.md)
  Returns the file’s owner account name.
- [func fileGroupOwnerAccountID() -> NSNumber?](nsdictionary/filegroupowneraccountid.md)
  Returns file’s group owner account ID.
- [func fileGroupOwnerAccountName() -> String?](nsdictionary/filegroupowneraccountname.md)
  Returns the file’s group owner account name.
- [func fileExtensionHidden() -> Bool](nsdictionary/fileextensionhidden.md)
  Returns a Boolean value indicating whether the file hides its extension.
- [func fileIsImmutable() -> Bool](nsdictionary/fileisimmutable.md)
  Returns a Boolean value indicating whether the file is immutable.
- [func fileIsAppendOnly() -> Bool](nsdictionary/fileisappendonly.md)
  Returns a Boolean value indicating whether the file is append only.
- [func fileSystemFileNumber() -> Int](nsdictionary/filesystemfilenumber.md)
  Returns the filesystem file number.
- [func fileSystemNumber() -> Int](nsdictionary/filesystemnumber.md)
  Returns the filesystem number.
- [func fileHFSTypeCode() -> OSType](nsdictionary/filehfstypecode.md)
  Returns file’s HFS type code.
- [func fileHFSCreatorCode() -> OSType](nsdictionary/filehfscreatorcode.md)
  Returns the file’s HFS creator code.
### Describing a Dictionary
- [var description: String](nsdictionary/description.md)
  A string that represents the contents of the dictionary, formatted as a property list.
- [var descriptionInStringsFileFormat: String](nsdictionary/descriptioninstringsfileformat.md)
  A string that represents the contents of the dictionary, formatted in `.strings` file format.
- [func description(withLocale: Any?) -> String](nsdictionary/description(withlocale:).md)
  Returns a string object that represents the contents of the dictionary, formatted as a property list.
- [func description(withLocale: Any?, indent: Int) -> String](nsdictionary/description(withlocale:indent:).md)
  Returns a string object that represents the contents of the dictionary, formatted as a property list.
### Initializers
- [convenience init(dictionary: NSDictionary)](nsdictionary/init(dictionary:)-4gc13.md)
### Default Implementations
- [Sequence Implementations](nsdictionary/sequence-implementations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSMutableDictionary](nsmutabledictionary.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByDictionaryLiteral](../Swift/ExpressibleByDictionaryLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSFastEnumeration](nsfastenumeration.md)
- [NSFetchRequestResult](../CoreData/NSFetchRequestResult.md)
- [NSMutableCopying](nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary)*