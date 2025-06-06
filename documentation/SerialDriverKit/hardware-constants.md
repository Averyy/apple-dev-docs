# Hardware Constants

**Framework**: SerialDriverKit

Configure your device with the appropriate parity and flow-control options.

## Topics

### Control Bits
- [PD_RS232_S_DTR](pd_rs232_s_dtr.md)
  The data-terminal-ready signal.
- [PD_RS232_S_DSR](pd_rs232_s_dsr.md)
  The data-set-ready signal.
- [PD_RS232_S_RTS](pd_rs232_s_rts.md)
  The request-to-send signal.
- [PD_RS232_S_CTS](pd_rs232_s_cts.md)
  The clear-to-send signal.
- [PD_RS232_S_RXO](pd_rs232_s_rxo.md)
  The receive-data signal.
- [PD_RS232_S_TXO](pd_rs232_s_txo.md)
  The transmit-data signal.
- [PD_RS232_S_DCD](pd_rs232_s_dcd.md)
  The data-carrier-detect signal.
### Parity Options
- [PD_RS232_PARITY_DEFAULT](pd_rs232_parity_default.md)
  The default parity setting.
- [PD_RS232_PARITY_NONE](pd_rs232_parity_none.md)
  No parity bit.
- [PD_RS232_PARITY_ODD](pd_rs232_parity_odd.md)
  An odd parity bit.
- [PD_RS232_PARITY_EVEN](pd_rs232_parity_even.md)
  An even parity bit.
- [PD_RS232_PARITY_MARK](pd_rs232_parity_mark.md)
  The mark state.
- [PD_RS232_PARITY_SPACE](pd_rs232_parity_space.md)
  The space state.
- [PD_RS232_PARITY_ANY](pd_rs232_parity_any.md)
  Discard the parity bit.

## See Also

- [HwGetModemStatus](iouserserial/hwgetmodemstatus.md)
  Gets the current status of the modem from the hardware.
- [SetModemStatus](iouserserial/setmodemstatus.md)
  Sets the modem status to the specified values.
- [HwResetFIFO](iouserserial/hwresetfifo.md)
  Sends a command to reset the specified device queues.
- [HwSendBreak](iouserserial/hwsendbreak.md)
  Sends a linebreak command to the device.
- [HwProgramBaudRate](iouserserial/hwprogrambaudrate.md)
  Sets the communication baud rate to the specified value.
- [HwProgramLatencyTimer](iouserserial/hwprogramlatencytimer.md)
  Sets the amount of time to wait before sending the current buffer to the device.
- [HwProgramMCR](iouserserial/hwprogrammcr.md)
  Configure the setings for the device’s modem control register (MCR).
- [HwProgramUART](iouserserial/hwprogramuart.md)
  Configure the settings for the device’s universal asynchronous receiver/transmitter (UART).


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/hardware-constants)*