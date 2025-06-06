# Hypervisor

**Framework**: Hypervisor  
**Kind**: module

Build virtualization solutions on top of a lightweight hypervisor, without third-party kernel extensions.

**Availability**:
- macOS 10.10+

#### Overview

Hypervisor provides C APIs so you can interact with virtualization technologies in user space, without writing kernel extensions (KEXTs). As a result, the apps you create using this framework are suitable for distribution on the [`Mac App Store`](https://developer.apple.comhttps://www.appstore.com/).

Use this framework to create and control hardware-facilitated virtual machines and virtual processors (VMs and vCPUs) from your entitled, sandboxed, user-space process. Hypervisor abstracts virtual machines as processes, and virtual processors as threads.

##### Requirements

The Hypervisor framework has the following requirements:

At runtime, determine whether the Hypervisor APIs are available on a particular machine with the sysctl command, passing `kern.hv_support` as an argument.

##### Virtual Resource Mapping

A guest is an operating system that runs on top of the virtual hardware. The operating system and processes that run the virtualized hardware are together called the host. Virtual hardware in the guest maps to specific resources on the host.

Each virtual machine corresponds to a process on the host. There can only be one virtual machine at a time per process; the virtual machine creates it with [`hv_vm_create(_:)`](hv_vm_create(_:).md).

Virtual CPUs (vCPUs) in a virtual machine map to POSIX threads. Create a new vCPU for the current thread with [`hv_vcpu_create(_:_:_:)`](hv_vcpu_create(_:_:_:).md). The vCPU runs when the thread calls [`hv_vcpu_run(_:)`](hv_vcpu_run(_:).md).

Hypervisor maps the physical memory in the guest to virtual memory of the host process. Create a new memory mapping with [`hv_vm_map(_:_:_:_:)`](hv_vm_map(_:_:_:_:).md). Access to memory outside the mapped range causes [`hv_vcpu_run(_:)`](hv_vcpu_run(_:).md) to exit. Emulate memory-mapped hardware by emulating the memory access on exit and re-enter the guest with [`hv_vcpu_run(_:)`](hv_vcpu_run(_:).md).

##### Example Vm Life Cycle

The following figure illustrates a simplified life cycle of creating and running a virtual machine with one or more virtual CPUs using the Hypervisor API.

![A flow diagram that represents the life cycle of a virtual machine.](https://docs-assets.developer.apple.com/published/bfee1ebf262231d5c3c11994026b7023/media-2916425%402x.png)

At the start of a task:

- Create a VM with [`hv_vm_create(_:)`](hv_vm_create(_:).md).
- Map a region in the virtual address space of the current task into the guest physical address space of the VM with [`hv_vm_map(_:_:_:_:)`](hv_vm_map(_:_:_:_:).md).
- Create one or more POSIX threads with `pthread_create(_:_:_:_:)`.

In each thread:

- Create a virtual CPU with [`hv_vcpu_create(_:_:_:)`](hv_vcpu_create(_:_:_:).md).
- Call [`hv_vcpu_run(_:)`](hv_vcpu_run(_:).md) to run the vCPU.

When a thread receives an exit event:

- Handle the event.
- Re-enter the guest with [`hv_vcpu_run(_:)`](hv_vcpu_run(_:).md) or destroy the vCPU with [`hv_vcpu_destroy(_:)`](hv_vcpu_destroy(_:).md).

After all threads finish:

- Unmap the memory region with [`hv_vm_unmap(_:_:)`](hv_vm_unmap(_:_:).md).
- Destroy the VM with [`hv_vm_destroy()`](hv_vm_destroy().md).

## Topics

### Platforms
- [Apple Silicon](apple-silicon.md)
  Create and run virtual machines on Apple silicon.
- [Intel-based Mac](intel-based-mac.md)
  Create and run virtual machines on Intel-based Mac computers.
### Entitlements
- [com.apple.security.hypervisor](../BundleResources/Entitlements/com.apple.security.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.hypervisor](../BundleResources/Entitlements/com.apple.vm.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.networking](../BundleResources/Entitlements/com.apple.vm.networking.md)
  A Boolean that indicates whether the app manages virtual network interfaces without escalating privileges to the root user.
- [com.apple.vm.device-access](../BundleResources/Entitlements/com.apple.vm.device-access.md)
  A Boolean value that indicates whether the app captures USB devices and uses them in the guest-operating system.
### Reference
- [Hypervisor Structures](hypervisor-structures.md)
- [Hypervisor Constants](hypervisor-constants.md)
- [Hypervisor Functions](hypervisor-functions.md)
- [Hypervisor Data Types](hypervisor-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Hypervisor)*