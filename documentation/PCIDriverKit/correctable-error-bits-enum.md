# Correctable Error Bits

**Framework**: PCIDriverKit  
**Role**: API Collection

Constants for the bits in the correctable error status register.

## Topics

### Constants
- [kIOPCICorrectableErrorBitReceiver](./kiopcicorrectableerrorbitreceiver.md)
  The bit number for a receiver error.
- [kIOPCICorrectableErrorBitBadTLP](./kiopcicorrectableerrorbitbadtlp.md)
  The bit number for a bad transaction layer packet error.
- [kIOPCICorrectableErrorBitBadDLLP](./kiopcicorrectableerrorbitbaddllp.md)
  The bit number for a bad DTLP error.
- [kIOPCICorrectableErrorBitReplayNumRollover](./kiopcicorrectableerrorbitreplaynumrollover.md)
  The bit number for an error that requires the retransmission of a packet.
- [kIOPCICorrectableErrorBitReplayTimerTimeout](./kiopcicorrectableerrorbitreplaytimertimeout.md)
  The bit number for a timeout error that involves the retransmission of a packet.
- [kIOPCICorrectableErrorBitAdvisoryNonFatal](./kiopcicorrectableerrorbitadvisorynonfatal.md)
  The bit number for an advisory error that is not fatal.
- [kIOPCICorrectableErrorBitCorrectedInternal](./kiopcicorrectableerrorbitcorrectedinternal.md)
  The bit number for an error that the device corrected internally.
- [kIOPCICorrectableErrorBitHeaderLogOverflow](./kiopcicorrectableerrorbitheaderlogoverflow.md)
  The bit number for a header log overflow error.

## See Also

### Getting Error Codes
- [Uncorrectable Error Bits](./uncorrectable-error-bits-enum.md)
  Constants for the bits in the uncorrectable error status register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/correctable-error-bits-enum)*