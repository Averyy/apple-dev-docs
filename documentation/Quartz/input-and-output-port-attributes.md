# Input and Output Port Attributes

**Framework**: Quartz

Attributes for input and output ports.

## Topics

### Constants
- [let QCPortAttributeTypeKey: String](qcportattributetypekey.md)
  The key for the port type. The associated value can be of any of the following constants: [`QCPortTypeBoolean`](qcporttypeboolean.md), [`QCPortTypeIndex`](qcporttypeindex.md), [`QCPortTypeNumber`](qcporttypenumber.md), [`QCPortTypeString`](qcporttypestring.md), [`QCPortTypeColor`](qcporttypecolor.md), [`QCPortTypeImage`](qcporttypeimage.md), or [`QCPortTypeStructure`](qcporttypestructure.md).
- [let QCPortAttributeNameKey: String](qcportattributenamekey.md)
  The key for the port name.
- [let QCPortAttributeMinimumValueKey: String](qcportattributeminimumvaluekey.md)
  The key for the port minimum value.
- [let QCPortAttributeMaximumValueKey: String](qcportattributemaximumvaluekey.md)
  The key for the port maximum value.
- [let QCPortAttributeDefaultValueKey: String](qcportattributedefaultvaluekey.md)
  The key for the port default value. You can use this key only for value ports (Boolean, Index, Number, Color and String).
- [let QCPortAttributeMenuItemsKey: String](qcportattributemenuitemskey.md)
  The key for the menu items.

## See Also

- [Patch Attributes](patch-attributes.md)
  Attributes for custom patches.
- [Port Input and Output Types](port-input-and-output-types.md)
  Data types for input and output ports.
- [Pixel Formats](pixel-formats.md)
  Supported image pixel formats.
- [Execution Arguments](execution-arguments.md)
  Arguments to the method [`execute(_:atTime:withArguments:)`](qcplugin/execute(_:attime:witharguments:).md).
- [struct QCPlugInExecutionMode](qcpluginexecutionmode.md)
  Execution modes for custom patches.
- [struct QCPlugInTimeMode](qcplugintimemode.md)
  Time modes for custom patches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/input-and-output-port-attributes)*