# FilePermissions

**Framework**: System  
**Kind**: struct

The access permissions for a file.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@frozen
struct FilePermissions
```

#### Overview

The following example creates an instance of the `FilePermissions` structure from a raw octal literal and compares it to a file permission created using named options:

```swift
let perms = FilePermissions(rawValue: 0o644)
perms == [.ownerReadWrite, .groupRead, .otherRead] // true
```

## Topics

### Owner Permissions
- [static var ownerRead: FilePermissions](filepermissions/ownerread.md)
  Indicates that the owner has read-only permission.
- [static var ownerWrite: FilePermissions](filepermissions/ownerwrite.md)
  Indicates that the owner has write-only permission.
- [static var ownerExecute: FilePermissions](filepermissions/ownerexecute.md)
  Indicates that the owner has execute-only permission.
- [static var ownerReadWrite: FilePermissions](filepermissions/ownerreadwrite.md)
  Indicates that the owner has read-write permission.
- [static var ownerReadExecute: FilePermissions](filepermissions/ownerreadexecute.md)
  Indicates that the owner has read-execute permission.
- [static var ownerWriteExecute: FilePermissions](filepermissions/ownerwriteexecute.md)
  Indicates that the owner has write-execute permission.
- [static var ownerReadWriteExecute: FilePermissions](filepermissions/ownerreadwriteexecute.md)
  Indicates that the owner has read, write, and execute permission.
### Group Permissions
- [static var groupRead: FilePermissions](filepermissions/groupread.md)
  Indicates that the group has read-only permission.
- [static var groupWrite: FilePermissions](filepermissions/groupwrite.md)
  Indicates that the group has write-only permission.
- [static var groupExecute: FilePermissions](filepermissions/groupexecute.md)
  Indicates that the group has execute-only permission.
- [static var groupReadWrite: FilePermissions](filepermissions/groupreadwrite.md)
  Indicates that the group has read-write permission.
- [static var groupReadExecute: FilePermissions](filepermissions/groupreadexecute.md)
  Indicates that the group has read-execute permission.
- [static var groupWriteExecute: FilePermissions](filepermissions/groupwriteexecute.md)
  Indicates that the group has write-execute permission.
- [static var groupReadWriteExecute: FilePermissions](filepermissions/groupreadwriteexecute.md)
  Indicates that the group has read, write, and execute permission.
### Other Permissions
- [static var otherRead: FilePermissions](filepermissions/otherread.md)
  Indicates that other users have read-only permission.
- [static var otherWrite: FilePermissions](filepermissions/otherwrite.md)
  Indicates that other users have write-only permission.
- [static var otherExecute: FilePermissions](filepermissions/otherexecute.md)
  Indicates that other users have execute-only permission.
- [static var otherReadWrite: FilePermissions](filepermissions/otherreadwrite.md)
  Indicates that other users have read-write permission.
- [static var otherReadExecute: FilePermissions](filepermissions/otherreadexecute.md)
  Indicates that other users have read-execute permission.
- [static var otherWriteExecute: FilePermissions](filepermissions/otherwriteexecute.md)
  Indicates that other users have write-execute permission.
- [static var otherReadWriteExecute: FilePermissions](filepermissions/otherreadwriteexecute.md)
  Indicates that other users have read, write, and execute permission.
### Special Permissions
- [static var setUserID: FilePermissions](filepermissions/setuserid.md)
  Indicates that the file is executed as the owner.
- [static var setGroupID: FilePermissions](filepermissions/setgroupid.md)
  Indicates that the file is executed as the group.
- [static var saveText: FilePermissions](filepermissions/savetext.md)
  Indicates that executable’s text segment should be kept in swap space even after it exits.
### Interacting with C APIs
- [init(rawValue: CModeT)](filepermissions/init(rawvalue:).md)
  Create a strongly-typed file permission from a raw C value.
- [let rawValue: CModeT](filepermissions/rawvalue-swift.property.md)
  The raw C file permissions.
- [typealias CModeT](cmodet.md)
  The C `mode_t` type.
- [FilePermissions.RawValue](filepermissions/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Debugging
- [var description: String](filepermissions/description.md)
  A textual representation of the file permissions.
- [var debugDescription: String](filepermissions/debugdescription.md)
  A textual representation of the file permissions, suitable for debugging.
### Comparing File Permissions
- [static func != (Self, Self) -> Bool](filepermissions/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func hash(into: inout Hasher)](filepermissions/hash(into:).md)
- [var hashValue: Int](filepermissions/hashvalue.md)
### Encoding File Permissions
- [init(from: any Decoder) throws](filepermissions/init(from:).md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt16`.
- [func encode(to: any Encoder) throws](filepermissions/encode(to:).md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `UInt16`.
### Performing Set Operations
- [init()](filepermissions/init.md)
  Creates an empty option set.
- [init<S>(S)](filepermissions/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](filepermissions/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [func contains(Self) -> Bool](filepermissions/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
- [func formIntersection(Self)](filepermissions/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formIntersection(Self)](filepermissions/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formSymmetricDifference(Self)](filepermissions/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
- [func formUnion(Self)](filepermissions/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](filepermissions/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func intersection(Self) -> Self](filepermissions/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func isDisjoint(with: Self) -> Bool](filepermissions/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [var isEmpty: Bool](filepermissions/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [func isStrictSubset(of: Self) -> Bool](filepermissions/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](filepermissions/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSubset(of: Self) -> Bool](filepermissions/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](filepermissions/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func remove(Self.Element) -> Self.Element?](filepermissions/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func subtract(Self)](filepermissions/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](filepermissions/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.
- [func symmetricDifference(Self) -> Self](filepermissions/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.
- [func union(Self) -> Self](filepermissions/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func update(with: Self.Element) -> Self.Element?](filepermissions/update(with:).md)
  Inserts the given element into the set.
### Type Aliases
- [FilePermissions.ArrayLiteralElement](filepermissions/arrayliteralelement.md)
  The type of the elements of an array literal.
- [FilePermissions.Element](filepermissions/element.md)
  The element type of the option set.
### Default Implementations
- [CustomDebugStringConvertible Implementations](filepermissions/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](filepermissions/customstringconvertible-implementations.md)
- [Equatable Implementations](filepermissions/equatable-implementations.md)
- [OptionSet Implementations](filepermissions/optionset-implementations.md)
- [RawRepresentable Implementations](filepermissions/rawrepresentable-implementations.md)
- [SetAlgebra Implementations](filepermissions/setalgebra-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct FileDescriptor](filedescriptor.md)
  An abstract handle to an input or output data resource, such as a file or a socket.
- [struct FilePath](filepath.md)
  Represents a location in the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepermissions)*