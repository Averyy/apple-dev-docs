# Error Codes

**Framework**: DriverKit

Determine the reason an operation fails.

## Topics

### No Error
- [kIOReturnSuccess](kioreturnsuccess.md)
### Errors
- [kIOReturnAborted](kioreturnaborted.md)
- [kIOReturnBadArgument](kioreturnbadargument.md)
- [kIOReturnBadMedia](kioreturnbadmedia.md)
- [kIOReturnBadMessageID](kioreturnbadmessageid.md)
- [kIOReturnBusy](kioreturnbusy.md)
- [kIOReturnCannotLock](kioreturncannotlock.md)
- [kIOReturnCannotWire](kioreturncannotwire.md)
- [kIOReturnDeviceError](kioreturndeviceerror.md)
- [kIOReturnDMAError](kioreturndmaerror.md)
- [kIOReturnError](kioreturnerror.md)
- [kIOReturnExclusiveAccess](kioreturnexclusiveaccess.md)
- [kIOReturnInternalError](kioreturninternalerror.md)
- [kIOReturnInvalid](kioreturninvalid.md)
- [kIOReturnIOError](kioreturnioerror.md)
- [kIOReturnIPCError](kioreturnipcerror.md)
- [kIOReturnIsoTooNew](kioreturnisotoonew.md)
- [kIOReturnIsoTooOld](kioreturnisotooold.md)
- [kIOReturnLockedRead](kioreturnlockedread.md)
- [kIOReturnLockedWrite](kioreturnlockedwrite.md)
- [kIOReturnMessageTooLarge](kioreturnmessagetoolarge.md)
- [kIOReturnNoBandwidth](kioreturnnobandwidth.md)
- [kIOReturnNoChannels](kioreturnnochannels.md)
- [kIOReturnNoCompletion](kioreturnnocompletion.md)
- [kIOReturnNoDevice](kioreturnnodevice.md)
- [kIOReturnNoFrames](kioreturnnoframes.md)
- [kIOReturnNoInterrupt](kioreturnnointerrupt.md)
- [kIOReturnNoMedia](kioreturnnomedia.md)
- [kIOReturnNoMemory](kioreturnnomemory.md)
- [kIOReturnNoPower](kioreturnnopower.md)
- [kIOReturnNoResources](kioreturnnoresources.md)
- [kIOReturnNoSpace](kioreturnnospace.md)
- [kIOReturnNotAligned](kioreturnnotaligned.md)
- [kIOReturnNotAttached](kioreturnnotattached.md)
- [kIOReturnNotFound](kioreturnnotfound.md)
- [kIOReturnNotOpen](kioreturnnotopen.md)
- [kIOReturnNotPermitted](kioreturnnotpermitted.md)
- [kIOReturnNotPrivileged](kioreturnnotprivileged.md)
- [kIOReturnNotReadable](kioreturnnotreadable.md)
- [kIOReturnNotReady](kioreturnnotready.md)
- [kIOReturnNotResponding](kioreturnnotresponding.md)
- [kIOReturnNotWritable](kioreturnnotwritable.md)
- [kIOReturnOffline](kioreturnoffline.md)
- [kIOReturnOverrun](kioreturnoverrun.md)
- [kIOReturnPortExists](kioreturnportexists.md)
- [kIOReturnRLDError](kioreturnrlderror.md)
- [kIOReturnStillOpen](kioreturnstillopen.md)
- [kIOReturnTimeout](kioreturntimeout.md)
- [kIOReturnUnderrun](kioreturnunderrun.md)
- [kIOReturnUnformattedMedia](kioreturnunformattedmedia.md)
- [kIOReturnUnsupported](kioreturnunsupported.md)
- [kIOReturnUnsupportedMode](kioreturnunsupportedmode.md)
- [kIOReturnVMError](kioreturnvmerror.md)

## See Also

- [OSDynamicCast](osdynamiccast.md)
  Casts an object safely to the specified type, if possible.
- [OSRequiredCast](osrequiredcast.md)
  Casts the object to the specified type, stopping the process if the object isn’t of the correct type.
- [IMPL](impl.md)
  Tells the system that the superclass implementation of this method runs in the kernel.
- [TYPE](type.md)
  Annotates a method declaration to indicate that it conforms to an existing method signature.
- [QUEUENAME](queuename.md)
  Tells the system to execute a method on the dispatch queue with the specified name.
- [SUPERDISPATCH](superdispatch.md)
  Tells the system to execute the superclass’ implementation of the current method in the kernel.
- [IIG_KERNEL](iig_kernel.md)
  Tells the system that the class or method runs inside the kernel.
- [LOCAL](local.md)
  Tells the system that the method runs locally in the driver extension’s process space.
- [LOCALONLY](localonly.md)
  Tells the system that the class or method runs locally in the driver extension’s process space.
- [C++ Runtime Support](c-runtime-support.md)
  Examine low-level types that DriverKit uses to support kernel-level operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/error-codes)*