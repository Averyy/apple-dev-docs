# FSDeactivateOptions

**Framework**: FSKit  
**Kind**: struct

Options that affect the behavior of deactivate methods.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct FSDeactivateOptions
```

## Topics

### Deactivation options
- [static var force: FSDeactivateOptions](fsdeactivateoptions/force.md)
  An option to force deactivation.
### Working with raw values
- [init(rawValue: Int)](fsdeactivateoptions/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](fsdeactivateoptions/equatable-implementations.md)
- [OptionSet Implementations](fsdeactivateoptions/optionset-implementations.md)
- [SetAlgebra Implementations](fsdeactivateoptions/setalgebra-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func activate(options: FSTaskOptions, replyHandler: (FSItem?, (any Error)?) -> Void)](fsvolume/operations/activate(options:replyhandler:).md)
  Activates the volume using the specified options.
- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [func deactivate(options: FSDeactivateOptions, replyHandler: ((any Error)?) -> Void)](fsvolume/operations/deactivate(options:replyhandler:).md)
  Tears down a previously initialized volume instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdeactivateoptions)*