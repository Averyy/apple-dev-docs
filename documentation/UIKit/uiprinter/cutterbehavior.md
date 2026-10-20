# UIPrinter.CutterBehavior

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the cutter behavior of a roll-fed printer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum CutterBehavior
```

```c
enum UIPrinterCutterBehavior : NSInteger;
```

## Topics

### Constants
- [UIPrinter.CutterBehavior.noCut](./cutterbehavior/nocut.md)
  Don’t cut the paper.
- [UIPrinter.CutterBehavior.printerDefault](./cutterbehavior/printerdefault.md)
  Use the printer’s default behavior.
- [UIPrinter.CutterBehavior.cutAfterEachPage](./cutterbehavior/cutaftereachpage.md)
  Cut the paper after each page.
- [UIPrinter.CutterBehavior.cutAfterEachCopy](./cutterbehavior/cutaftereachcopy.md)
  Cut the paper after each copy of the document.
- [UIPrinter.CutterBehavior.cutAfterEachJob](./cutterbehavior/cutaftereachjob.md)
  Cut the paper after each print job finishes.
### Initializers
- [init?(rawValue: Int)](./cutterbehavior/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinter/cutterbehavior)*