# FileDescriptor.OpenOptions

**Framework**: System  
**Kind**: struct

Options that specify behavior for a newly-opened file.

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
struct OpenOptions
```

## Topics

### Specifying Options
- [static var append: FileDescriptor.OpenOptions](filedescriptor/openoptions/append.md)
  Indicates that each write operation appends to the file.
- [static var closeOnExec: FileDescriptor.OpenOptions](filedescriptor/openoptions/closeonexec.md)
  Indicates that executing a program closes the file.
- [static var create: FileDescriptor.OpenOptions](filedescriptor/openoptions/create.md)
  Indicates that opening the file creates the file if it doesn’t exist.
- [static var eventOnly: FileDescriptor.OpenOptions](filedescriptor/openoptions/eventonly.md)
  Indicates that opening the file monitors a file for changes.
- [static var exclusiveCreate: FileDescriptor.OpenOptions](filedescriptor/openoptions/exclusivecreate.md)
  Indicates that opening the file creates the file, expecting that it doesn’t exist.
- [static var exclusiveLock: FileDescriptor.OpenOptions](filedescriptor/openoptions/exclusivelock.md)
  Indicates that opening the file atomically obtains an exclusive lock.
- [static var noFollow: FileDescriptor.OpenOptions](filedescriptor/openoptions/nofollow.md)
  Indicates that opening the file doesn’t follow symlinks.
- [static var nonBlocking: FileDescriptor.OpenOptions](filedescriptor/openoptions/nonblocking.md)
  Indicates that opening the file doesn’t wait for the file or device to become available.
- [static var sharedLock: FileDescriptor.OpenOptions](filedescriptor/openoptions/sharedlock.md)
  Indicates that opening the file atomically obtains a shared lock on the file.
- [static var symlink: FileDescriptor.OpenOptions](filedescriptor/openoptions/symlink.md)
  Indicates that opening the file opens symbolic links instead of following them.
- [static var truncate: FileDescriptor.OpenOptions](filedescriptor/openoptions/truncate.md)
  Indicates that opening the file truncates the file if it exists.
### Interacting with C APIs
- [init(rawValue: CInt)](filedescriptor/openoptions/init(rawvalue:).md)
  Create a strongly-typed options value from raw C options.
- [var rawValue: CInt](filedescriptor/openoptions/rawvalue-swift.property.md)
  The raw C options.
- [FileDescriptor.OpenOptions.RawValue](filedescriptor/openoptions/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Debugging
- [var description: String](filedescriptor/openoptions/description.md)
  A textual representation of the open options.
- [var debugDescription: String](filedescriptor/openoptions/debugdescription.md)
  A textual representation of the open options, suitable for debugging.
### Comparing Open Options
- [static func != (Self, Self) -> Bool](filedescriptor/openoptions/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func hash(into: inout Hasher)](filedescriptor/openoptions/hash(into:).md)
- [var hashValue: Int](filedescriptor/openoptions/hashvalue.md)
### Encoding Open Options
- [init(from: any Decoder) throws](filedescriptor/openoptions/init(from:).md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int32`.
- [func encode(to: any Encoder) throws](filedescriptor/openoptions/encode(to:).md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int32`.
### Performing Set Operations
- [init()](filedescriptor/openoptions/init.md)
  Creates an empty option set.
- [init<S>(S)](filedescriptor/openoptions/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](filedescriptor/openoptions/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [func contains(Self) -> Bool](filedescriptor/openoptions/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
- [func formIntersection(Self)](filedescriptor/openoptions/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formIntersection(Self)](filedescriptor/openoptions/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formSymmetricDifference(Self)](filedescriptor/openoptions/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
- [func formUnion(Self)](filedescriptor/openoptions/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](filedescriptor/openoptions/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func intersection(Self) -> Self](filedescriptor/openoptions/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func isDisjoint(with: Self) -> Bool](filedescriptor/openoptions/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [var isEmpty: Bool](filedescriptor/openoptions/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [func isStrictSubset(of: Self) -> Bool](filedescriptor/openoptions/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](filedescriptor/openoptions/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSubset(of: Self) -> Bool](filedescriptor/openoptions/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](filedescriptor/openoptions/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func remove(Self.Element) -> Self.Element?](filedescriptor/openoptions/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func subtract(Self)](filedescriptor/openoptions/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](filedescriptor/openoptions/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.
- [func symmetricDifference(Self) -> Self](filedescriptor/openoptions/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.
- [func union(Self) -> Self](filedescriptor/openoptions/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func update(with: Self.Element) -> Self.Element?](filedescriptor/openoptions/update(with:).md)
  Inserts the given element into the set.
### Type Aliases
- [FileDescriptor.OpenOptions.ArrayLiteralElement](filedescriptor/openoptions/arrayliteralelement.md)
  The type of the elements of an array literal.
- [FileDescriptor.OpenOptions.Element](filedescriptor/openoptions/element.md)
  The element type of the option set.
### Type Properties
- [static var directory: FileDescriptor.OpenOptions](filedescriptor/openoptions/directory.md)
  Indicates that opening the file only succeeds if the file is a directory.
### Default Implementations
- [CustomDebugStringConvertible Implementations](filedescriptor/openoptions/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](filedescriptor/openoptions/customstringconvertible-implementations.md)
- [Equatable Implementations](filedescriptor/openoptions/equatable-implementations.md)
- [OptionSet Implementations](filedescriptor/openoptions/optionset-implementations.md)
- [RawRepresentable Implementations](filedescriptor/openoptions/rawrepresentable-implementations.md)
- [SetAlgebra Implementations](filedescriptor/openoptions/setalgebra-implementations.md)

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

- [static func open(FilePath, FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions?, retryOnInterrupt: Bool) throws -> FileDescriptor](filedescriptor/open(_:_:options:permissions:retryoninterrupt:)-4ql4b.md)
  Opens or creates a file for reading or writing.
- [static func open(UnsafePointer<CChar>, FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions?, retryOnInterrupt: Bool) throws -> FileDescriptor](filedescriptor/open(_:_:options:permissions:retryoninterrupt:)-5t3xn.md)
  Opens or creates a file for reading or writing.
- [FileDescriptor.AccessMode](filedescriptor/accessmode.md)
  The desired read and write access for a newly opened file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/openoptions)*