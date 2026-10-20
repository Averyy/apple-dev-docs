# FSDeactivateOptions

**Framework**: FSKit  
**Kind**: struct  
**Role**: Structure

Options that affect the behavior of deactivate methods.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct FSDeactivateOptions
```

```c
enum FSDeactivateOptions : NSInteger;
```

## Topics

### Deactivation options
- [static var force: FSDeactivateOptions](./fsdeactivateoptions/force.md)
  An option to force deactivation.
### Working with raw values
- [init(rawValue: Int)](./fsdeactivateoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Handling activation and deactivation
- [class FSItem](./fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [class FSActivateResult](./fsactivateresult.md)
  The result of an activate call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdeactivateoptions)*